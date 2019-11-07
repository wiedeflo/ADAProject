'''
File name: constants.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 03/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains constants such as file paths, columns names,...
'''
###########################################################################################################
################################################ DATABASES ################################################
###########################################################################################################

# Data Folder
DATA_PATH = '../data/'

# General column names
AREA_NAME = 'community_area_name'
AREA_NUM = 'community_area_num'

# Food inspection
FOOD_INSPECTIONS_PATH = DATA_PATH + 'food-inspections.csv'
FOOD_INSPECTIONS_COL_NAMES = ['inspection_id', 'DBA_name', 'AKA_name', 'license_num', 'facility_type', 'risk', 'address', 'city',
                              'state', 'zip', 'inspection_date', 'inspection_type', 'result', 'violations', 'lat', 'lng',
                              'location', 'historical_wards', 'zip_codes', 'community_areas', 'census_tracts', 'wards']

# Socio-economic indicators
SOCIO_ECONOMIC_INDICATORS_PATH = DATA_PATH + 'Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv'
SOCIO_ECONOMIC_COL_NAMES = ['community_area_num', 'community_area_name', 'housing_crowded_perc', 'housholds_below_poverty_perc', 'aged_16_or_more_unemployed_perc', 'aged_25_or_more_without_high_school_diploma_perc', 'aged_under_18_or_over_64_perc', 'per_capita_income', 'hardship_idx']

# Life expectancy
LIFE_EXPECTANCY_PATH = DATA_PATH + 'Public_Health_Statistics-_Life_Expectancy_By_Community_Area.csv'
LIFE_EXPECTANCY_COL_NAMES = ['community_area_num', 'community_area_name', 'life_exp_1990', 'lower_95_perc_CI_1990', 'upper_95_perc_CI_1990', 'life_exp_2000', 'lower_95_perc_CI_2000', 'upper_95_perc_CI_2000', 'life_exp_2010', 'lower_95_perc_CI_2010', 'upper_95_perc_CI_2010']

# Chicago areas region bounds
AREAS_PATH = DATA_PATH + 'Boundaries - Community Areas (current)/geo_export_3ffbc00d-9720-4c2b-b3c0-ed098b3b9ae7.shp'

###########################################################################################################
######################################## LNG/LAT FROM CHICAGO AREA ########################################
###########################################################################################################

# Chicago area
LAT_LNG_HTML_POSITION_START = 'window.APP_INITIALIZATION_STATE=[[['
LAT_LNG_HTML_POSITION_STOP = ']'
CHICAGO_AREA_URL = 'https://www.google.com/maps/place/%s,+Chicago,+IL,+USA'
CHICAGO_ADDRESS = "Chicago, Illinois, United States"

MONTCLAIRE_AREA_LAT = 41.929681
MONTCLAIRE_AREA_LNG = -87.799306
WASHINGTON_HEIGHT_AREA_LAT = 41.718415
WASHINGTON_HEIGHT_AREA_LNG = -87.642884

# Geopy lib
GEOPY_USER_AGENT = "not sure what to write : TODO"
GEOPY_TIMEOUT = 3
