'''
File name: areas_handler.py
Date created: 07/11/2019
Date last modified: 25/11/2019
Python Version: 3.7.4
Contains methods to get the area in Chicago of a longitude/latitude pair
'''

import os
import re 
import math
import pandas as pd

import geopy
from geopy.geocoders import Nominatim

from shapely.geometry import Point
from shapely.geometry import Polygon

from utils import constants as cst
from utils import web_scraping_google_maps

def get_lat_lng_from_address(address, cleaned=False):
    """
    Retrieve the latitude and the longitude from a Chicago area. Uses geopy to retrieve this information.
    :param area: string
    :return: a list containing 2 floats (the latitude and the longitude)
    """
            
    complete_addr = address + ", " + cst.CHICAGO_ADDRESS
    loc = Nominatim(user_agent=cst.GEOPY_USER_AGENT, timeout=cst.GEOPY_TIMEOUT).geocode(complete_addr)
    
    lat, lng = None, None 
    
    if not loc:
        if not cleaned :
            # Try cleaning it :
            clean_addr = get_clean_address_new(address)
            [lat, lng] = get_lat_lng_from_address(clean_addr, cleaned=True)
        else:
            lat, lng = None, None 
    else:
        lat, lng = loc.latitude, loc.longitude
    
    return [lat, lng]

def get_clean_address(address):
    """
    Some addresses are in an unrecognizable format, this method cleans them e.g. '3459 S OGDEN AVE' becomes '3459 OGDEN'
    :param address: string
    :return: a string containing the cleaned address
    """
    
    # Split the address into a list of strings
    addr_split = address.split(' ')
    
    # Remove all unrecognizable strings from the address
    for unknown_str in cst.UNKNOWN_ADDR_STRINGS:
        
        # There might be multiple same strings in the address
        while unknown_str in addr_split:
            addr_split.remove(unknown_str)
    
    # Join the remaining address
    clean_address = ' '.join(addr_split)
    
    return clean_address

def get_clean_address_new(address):
    """
    Some addresses are in an unrecognizable format, this method cleans them e.g. '3459 S OGDEN AVE' becomes '3459 OGDEN'
    :param address: string
    :return: a string containing the cleaned address
    """
    
    # Split the address into a list of strings
    addr_split = address.split(' ')
    
    # Replace all abbreviations and knwon problems
    addr_split = [cst.KNOWN_ADDR_STRINGS.get(add) if add in cst.KNOWN_ADDR_STRINGS else add for add in addr_split]
    
    # Replace typos
    addr_split = [cst.TYPO_FIXES.get(add) if add in cst.TYPO_FIXES else add for add in addr_split]
        
    # Remove things in brackets
    addr_split = [re.sub('\(.*\)', '', add) for add in addr_split]
        
    # Join the remaining address
    clean_address = ' '.join(addr_split)
    
    # Remove unneccesary whitespace
    while '  ' in clean_address:
        clean_address = clean_address.replace('  ',' ')
    
    # Replace the remaining adresses with a manually constructed dict
    for rem in cst.UNKNOWN_ADDR_SUBSTRINGS:
        clean_address = clean_address.replace(rem, cst.UNKNOWN_ADDR_SUBSTRINGS.get(rem))
    
    return clean_address

def get_area_num_from_lng_lat(lat, lng, areas_DF):
    '''
    get the area number from a longitude latitude pair, using the parameter "areas_DF" 
    :param lat: a float
    :param lng: a float
    :param areas_DF: pandas.DataFrame
    :return: the area number of (lng, lat) location
    '''
    
    # attention : points are in form (lng, lat) in areas_DF
    loc = Point(lng, lat)
    
    all_areas_as_polygones = areas_DF['geometry']
    area_with_loc = all_areas_as_polygones.contains(loc)
    
    if not area_with_loc.any():
        return math.nan
        #raise ValueError('No area with lat: %f and lng: %f'%(lat, lng))
            
    area_num = areas_DF[area_with_loc][cst.AREA_NUM].values[0]
    
    return int(area_num)

def get_unknown_locations(food_unknown_loc, load_if_possible = True):
    """
    Get the lat/lng of unknown addresses in a dataframe
    :param food_unknown_loc: a pandas.DataFrame 
    :return: a pd.DataFrame containing the previously unknown location's along with their latitude and longitude, or NaN if this value could not be found.
    """
    
    # Load unknown locations if file already exists :
    if os.path.exists(cst.UNKNOWN_LOC_PATH) and load_if_possible:
        unknown_locations = pd.read_pickle(cst.UNKNOWN_LOC_PATH)
     
    # Otherwise create the file
    else:
        # Compute the missing locations
        # No need for duplicate queries, so we just keep the unique addresses
        unknown_locations = pd.DataFrame(food_unknown_loc['address'].unique(), columns=['address'])
        
        # Retrieve 'lat' and 'lng' values of an address and append them to 'unknown_locations' dataframe
        unknown_locations[['lat', 'lng']] = unknown_locations['address'].apply(lambda addr: pd.Series(get_lat_lng_from_address(addr)))

        # Save them as pickle file
        unknown_locations.to_pickle(cst.UNKNOWN_LOC_PATH)
        
    return unknown_locations

def get_locations_with_area(food_inspections_DF, areas_DF, load_if_possible = True):
    """
    Load the food inspections with area code if it exists, otherwise compute the area code for each food inspection and save it
    :param food_inspections_DF: a pandas.DataFrame with the food inspections
    :param areas_DF: a pandas.DataFrame with the areas
    :param load_if_possible: a boolean variable set to true by default
    :return: a pd.DataFrame containing the food inspections with their area numbers
    """
    if os.path.exists(cst.FOOD_INSPECTIONS_AREA_PICKLE) and load_if_possible:
         # Try loading the food inspections with area code :
        food_inspections_DF = pd.read_pickle(cst.FOOD_INSPECTIONS_AREA_PICKLE)
        
    else:
        # Compute area code for each entry
        food_inspections_DF[cst.AREA_NUM] = food_inspections_DF.apply(lambda row: get_area_num_from_lng_lat(row['lat'], row['lng'], areas_DF), axis=1)
        
        # Save as pickle
        food_inspections_DF.to_pickle(cst.FOOD_INSPECTIONS_AREA_PICKLE)
        
    return food_inspections_DF