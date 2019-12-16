'''
File name: areas_handler.py
Date created: 21/11/2019
Date last modified: 24/11/2019
Python Version: 3.7.4
Methods to visualize a map of Chicago by areas and with specific attributes
'''

import folium
from folium import plugins
import json
import math
import datetime

from utils import constants as cst
from utils import interactive_plot_handler
from utils.interactive_plot_handler import region_to_color, name_to_region

def create_chicago_map(with_community_areas=False, with_regions=False, areas_DF=None):
    """
    Creates a map of Chicago, highlighting the community areas
    :return: a folium map
    """
    
    # Set parameters for map with/without regions
    dragging_enabled = False if with_regions else True
    max_zoom = 10 if with_regions else 16
    min_zoom = 10 if with_regions else 8
    zoomControl = False if with_regions else True
    
    # Initialize basic map
    map_chicago = folium.Map(location = cst.CHICAGO_LOCATION, 
                             max_bounds=True,
                             min_lat=cst.CHICAGO_MIN_LAT,
                             max_lat=cst.CHICAGO_MAX_LAT,
                             min_lon=cst.CHICAGO_MIN_LNG,
                             max_lon=cst.CHICAGO_MAX_LNG,
                             max_zoom=max_zoom,
                             min_zoom=min_zoom,
                             zoom_start=10,
                             dragging=dragging_enabled,
                             zoomControl=zoomControl
                            )
    
    if with_community_areas:
        #load region data
        regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
        
        for feat in regiondata['features']:
            feat['properties']['community'] = feat['properties']['community'].title()
            
        if with_regions:
            #create heatmap
            folium.GeoJson(
                regiondata,
                style_function=lambda feature: {
                    'fillColor': my_color_function(feature),
                    'fillOpacity':0.7,
                    'color' : 'black',
                    'weight' : 1,
                    'dashArray' : '1, 1'
                    }
                ).add_to(map_chicago)
            
            choro = folium.Choropleth(geo_data=regiondata, 
                                      columns=[cst.AREA_NUM],
                                      fill_opacity=0,
                                      key_on='feature.properties.area_numbe').add_to(map_chicago)

            choro.geojson.add_child(folium.features.GeoJsonTooltip(['community']))
        else:
            #create heatmap
            choro = folium.Choropleth(geo_data=regiondata, 
                                      columns=[cst.AREA_NUM],
                                      fill_opacity=0.3,
                                      key_on='feature.properties.area_numbe').add_to(map_chicago)

            choro.geojson.add_child(folium.features.GeoJsonTooltip(['community']))

    return map_chicago

def my_color_function(feature):
    """Maps low values to green and hugh values to red."""
    area = feature['properties']['community']
    region = name_to_region[area.lower()]
    return region_to_color[region] 

def add_locations(map_chicago, unknown_locations, food_inspections_DF):
    """
    Adds specific locations to the map
    :param map_chicago: folium map of Chicago
    :param unknown_locations: array of unknown locations to highlight
    :param food_inspections_DF: pandas.DataFrame with the food inspections
    :return: folium map with markers
    """
    # Add region overlay
    regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
    folium.GeoJson(regiondata).add_to(map_chicago)
    
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

def heat_map(dataframe, title, area_column, data_column, good_indicator = False, rename_mapping=None):
    """
    Plot number of inspections per community area as a heatmap
    :param dataframe: dataframe containing area numbers and used data
    :param title: Title of the heatmap
    :param area_column: Column of the dataframe containing area information
    :param data_column: Column of the dataframe containing data
    :return: folium heatmap of inspections per area
    """

    if good_indicator:
        colors = "YlGn"
    else:
        colors="YlOrRd"
        
    if rename_mapping:
        dataframe = dataframe.rename(columns=rename_mapping)
        
        if data_column in rename_mapping.keys():
            data_column = rename_mapping[data_column]
       
    #load new map
    map_chicago = create_chicago_map() 

    #load region data
    regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
    
    for feat in regiondata['features']:
        feat['properties']['community'] = feat['properties']['community'].title()
        
        if dataframe[dataframe[area_column] == feat['properties']['area_numbe']].empty:
            feat['properties'][data_column] = 'NaN'
        else:
            feat['properties'][data_column] = str(dataframe[dataframe[area_column] == feat['properties']['area_numbe']][data_column].values[0])
                
    #create heatmap
    choro = folium.Choropleth(geo_data=regiondata, data=dataframe,
                 columns=[area_column, data_column],
                 key_on='feature.properties.area_numbe',
                 fill_color=colors, fill_opacity=0.7,nan_fill_color='grey',  line_opacity=0.2,
                 legend_name=title).add_to(map_chicago)
    
    choro.geojson.add_child(folium.features.GeoJsonTooltip(['community', data_column]))
    
    return map_chicago


#tried time map and failed
def timed_heatmap(dataframe, areas_DF):
                  
    #load new map
    map_chicago = create_chicago_map() 

    #load region data
    #regiondata = json.load(open(cst.AREAS_GEOJSON_PATH))
                  
    #create styledict
    styledict = {}
    for row in dataframe.values:
        inner_dict = {}
        for column in dataframe:
            if column != cst.AREA_NUM:
                epoch = str(int(datetime.datetime(column, 1, 1,0,0).timestamp()))
                inner_dict[epoch] = {'color': '#ffffff', 'opacity': 1}
        styledict[str(int(row[0])-1)] = inner_dict
        
    #print(areas_DF.to_json())
    
    
                  
    #print(styledict)
    folium.plugins.TimeSliderChoropleth(data=areas_DF.to_json(), overlay = True, styledict = styledict).add_to(map_chicago)
    return map_chicago