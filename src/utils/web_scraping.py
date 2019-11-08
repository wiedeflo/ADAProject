'''
File name: web_scraping.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 03/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains methods to retrieve the latitude and longitude of a Chicago city area
'''

import requests
import geopy
from geopy.geocoders import Nominatim
from utils import constants as cst

def get_lat_lng_from_area_name(area):
    """
    Retrieve the latitude and the longitude from a Chicago area. Uses geopy to retrieve this information.
    :param area: string
    :return: a list containing 2 floats (the latitude and the longitude)
    """
        
    complete_area = area + ", " + cst.CHICAGO_ADDRESS
    loc = Nominatim(user_agent=cst.GEOPY_USER_AGENT, timeout=cst.GEOPY_TIMEOUT).geocode(complete_area)
    
    if not loc:
        lat, lng = None, None # get_lat_lng_from_area_name_google_maps(area)
    else:
        lat, lng = loc.latitude, loc.longitude
    
    
    return [lat, lng]
    

def get_lat_lng_from_address_name_google_maps(address):
    """
    Retrieve the latitude and the longitude from a Chicago area.
    :param area: string
    :return: a list containing 2 floats (the latitude and the longitude)
    """
    
    # Complete the address by adding "Chicago, United States"
    complete_address = address + " " + cst.CHICAGO_ADDRESS
    
    # get url to request
    url = get_url_from_address_google_maps(complete_address)
    
    # get response from url
    r = requests.get(url)
    
    # parse response text to find string containing latitude and longitude
    lat_and_lng = r.text.partition(cst.LAT_LNG_HTML_POSITION_START)[2].partition(cst.LAT_LNG_HTML_POSITION_STOP)[0]
    
    # retrieve lat and lng
    lng, lat = lat_and_lng.split(',')[1:]
    
    return lat, lng

def get_url_from_address_google_maps(address):
    """
    Retrieve the url corresponding to a 'google maps' query for a Chicago city area
    :param area: string
    :return: a string
    """
    separator = '+'
    
    # get a string containing the words of the area joined by a '+', e.g. "Rogers Park" becomes "Rogers+Park"
    address_formatted = separator.join(address.split(" "))
        
    # return the url for the area
    url = cst.CHICAGO_AREA_URL % (address_formatted)
    return url