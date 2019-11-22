'''
File name: areas_handler.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 21/11/2019
Date last modified: ...
Python Version: 3.7.4
Methods to visualize a map of Chicago by areas and with specific attributes
'''

import folium
import json
import math

from utils import constants as cst

def create_chicago_map():
    """
    Creates a map of Chicago, highlighting the community areas
    :return: a folium map
    """
    map_chicago = folium.Map(location = cst.CHICAGO_LOCATION)
    regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
    folium.GeoJson(regiondata).add_to(map_chicago)
    return map_chicago

def add_locations(map_chicago, unknown_locations, food_inspections_DF):
    """
    Adds specific locations to the map
    :param map_chicago: folium map of Chicago
    :param unknown_locations: array of unknown locations to highlight
    :param food_inspections_DF: pandas.DataFrame with the food inspections
    :return: folium map with markers
    """
    # Create two groups : known and unknown locations
    uncertain_locations_feature=folium.FeatureGroup(name='Uncertain Points', show=False)
    map_chicago.add_child(uncertain_locations_feature)
    certain_locations_feature=folium.FeatureGroup(name='Certain Points', show=False)
    map_chicago.add_child(certain_locations_feature)
    folium.LayerControl().add_to(map_chicago)
    
    # Add all unknown locations to the 'Uncertain Points' group
    for index, entry in unknown_locations.iterrows():
        if not math.isnan(entry['lat']):
            folium.Marker([entry['lat'], entry['lng']]).add_to(uncertain_locations_feature)

    # Add first 1000 known locations to the 'Certain Points' group (just for comparison)
    for index, entry in food_inspections_DF[:1000].iterrows():
        if not math.isnan(entry['lat']):
            folium.Marker([entry['lat'], entry['lng']], icon=folium.Icon(color='red')).add_to(certain_locations_feature)
    
    return map_chicago

def inspections_heat_map(inspection_counts):
    """
    Plot number of inspections per community area as a heatmap
    :param map_chicago: folium map of Chicago
    :param inspection_counts: pandas.DataFrame with columns 'community_area_num' and 'index'
    :return: folium heatmap of inspections per area
    """
    
    map_chicago = create_chicago_map()
    regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
    folium.GeoJson(regiondata).add_to(map_chicago)

    folium.Choropleth(geo_data=regiondata, data=inspection_counts,
                 columns=['index', cst.AREA_NUM],
                 key_on='feature.properties.area_numbe',
                 fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
                 legend_name='Number of inspections per region').add_to(map_chicago)
    
    return map_chicago