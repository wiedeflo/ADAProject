'''
File name: areas_handler.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 07/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains methods to get the area in Chicago of a longitude/latitude pair
'''

from shapely.geometry import Point
from shapely.geometry import Polygon

from utils import constants as cst

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
        raise ValueError('No area with lat: %f and lng: %f'%(lat, lng))
            
    area_num = areas_DF[area_with_loc][cst.AREA_NUM].values[0]
    
    return int(area_num)