'''
File name: areas_handler.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 07/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains methods to get the area in Chicago of a longitude/latitude pair
'''

import geopy
from geopy.geocoders import Nominatim
from shapely.geometry import Point
from shapely.geometry import Polygon

from utils import constants as cst
from utils import web_scraping_google_maps

import math
import re

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
            clean_addr = get_clean_address(address)
            [lat, lng] = get_lat_lng_from_address(clean_addr, cleaned=True)
        else:
            # TODO : create method similar to : web_scraping_google_maps.get_lat_lng_from_area_name(area) or find alt.
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
    
    addr_split = [cst.KNOWN_ADDR_STRINGS.get(add) if add in cst.KNOWN_ADDR_STRINGS else add for add in addr_split]
    
    addr_split = [cst.TYPO_FIXES.get(add) if add in cst.TYPO_FIXES else add for add in addr_split]
        
    addr_split = [re.sub('\(.*\)', '', add) for add in addr_split]
    
    for rem in cst.UNKNOWN_ADDR_SUBSTRINGS:
        address = address.replace(rem, cst.UNKNOWN_ADDR_SUBSTRINGS.get(rem))
    
    # Join the remaining address
    clean_address = ' '.join(addr_split)
    
    while '  ' in clean_address:
        clean_address = clean_address.replace('  ',' ')
    #clean_address = clean_address.replace(' ,',',')
    
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