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
FOOD_INSPECTIONS_COL_NAMES = ['inspection_id', 'DBA_name', 'AKA_name', 'license_num', 'facility_type', 'risk', 'address', 'city', 'state', 'zip', 'inspection_date', 'inspection_type', 'result', 'violations', 'lat', 'lng', 'location', 'historical_wards_2003-2015', 'zip_codes', 'community_area', 'census_tracts', 'wards']

# Socio-economic indicators
SOCIO_ECONOMIC_INDICATORS_PATH = DATA_PATH + 'Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv'
SOCIO_ECONOMIC_COL_NAMES = ['community_area_num', 'community_area_name', 'housing_crowded_perc', 'housholds_below_poverty_perc', 'aged_16_or_more_unemployed_perc', 'aged_25_or_more_without_high_school_diploma_perc', 'aged_under_18_or_over_64_perc', 'per_capita_income', 'hardship_idx']

# Life expectancy
LIFE_EXPECTANCY_PATH = DATA_PATH + 'Public_Health_Statistics-_Life_Expectancy_By_Community_Area.csv'
LIFE_EXPECTANCY_COL_NAMES = ['community_area_num', 'community_area_name', 'life_exp_1990', 'lower_95_perc_CI_1990', 'upper_95_perc_CI_1990', 'life_exp_2000', 'lower_95_perc_CI_2000', 'upper_95_perc_CI_2000', 'life_exp_2010', 'lower_95_perc_CI_2010', 'upper_95_perc_CI_2010']

SOCIOECONOMIC_METRICS = ['housing_crowded_perc', 'housholds_below_poverty_perc', 'aged_16_or_more_unemployed_perc', 'aged_25_or_more_without_high_school_diploma_perc', 'per_capita_income', 'hardship_idx','life_exp_2010', 'aged_under_18_or_over_64_perc']

# Chicago areas region bounds
AREAS_PATH = DATA_PATH + 'Boundaries - Community Areas (current)/geo_export.shp'

# Chicago areas ragion bounds as GeoJson
AREAS_GEOJSON_PATH = DATA_PATH + 'Boundaries - Community Areas (current).json'

###########################################################################################################
######################################## LNG/LAT FROM CHICAGO AREA ########################################
###########################################################################################################

# Chicago area
LAT_LNG_HTML_POSITION_START = 'window.APP_INITIALIZATION_STATE=[[['
LAT_LNG_HTML_POSITION_STOP = ']'
CHICAGO_AREA_URL = 'https://www.google.com/maps/place/%s,+Chicago,+IL,+USA'
CHICAGO_ADDRESS = "Illinois, United States"

MONTCLAIRE_AREA_LAT = 41.929681
MONTCLAIRE_AREA_LNG = -87.799306
WASHINGTON_HEIGHT_AREA_LAT = 41.718415
WASHINGTON_HEIGHT_AREA_LNG = -87.642884

# Geopy lib
GEOPY_USER_AGENT = "not sure what to write : TODO"
GEOPY_TIMEOUT = 10

# Strings that we manually replace as they contain insufficient information
UNKNOWN_ADDR_SUBSTRINGS = {'/SIDE DRIVE' : '', "O'HARE FIELD" : "O'HARE", 'SITE 322' : '', 'Rockwell AVENUE' : 'Rockwell Street', 'Doty' : 'Doty AVENUE', '(11156 S)' : '', '(St. Maurice)' : '', '2104AB-2108A SOUTH ARCHER AVENUE' : '2108 South Archer Avenue', 'WEST WEST' : 'WEST', 'DELANO WEST COURT': 'DELANO Court', 'DELANO EAST COURT': 'DELANO Court', '108 WEST PARK' : '108 West Park Avenue, Elmhurst', '4934 SOUTH Wabash BUILDING' : '4934 South Wabash Avenue', '3901 SOUTH DR MARTIN LUTHER KING JR' : '3901 SOUTH DR MARTIN LUTHER KING Junior Drive', '8306 SOUTH LAWRENCE AVENUE' : '8306 WEST LAWRENCE AVENUE', '1332 WEST DRIVING PARK ROAD BSMT': '1332 West Irving Park Road', '2300 NORTH Childrens Plaza PLAZA BUILDING' : '720 West Fullerton Parkway', '3107 SOUTH 71st STREET BSMT' : '3107 West 71st Street', '2920 SOUTH WENWORTH SITE 2' : '2920 South Wentworth Avenue', '6601 MARTIN FRANCE' : '6601 MARTIN FRANCE CIRCLE', '13946 SOUTH CHIPPEWA' : '13946 SOUTH CHIPPEWA AVENUE', '2217 WEST CRYSTAL STREET APT 2' : '2217 WEST CRYSTAL STREET', '1413 SOUTH 11 TH AVENUE':'1413 SOUTH 11TH AVENUE', '4500 SOUTH WOODS STREET' : '4500 SOUTH WOOD STREET', '425 EAST MC FETRIDGE BUILDING':'425 East McFetridge Drive', '4000 NORTH OHARE AIRPORT':'4000 NORTH OHARE', '3455-3459 SOUTH OGDEN AVENUE' : '3455 Ogden Avenue'}

# Known Abbreviations and some minor address fixed
KNOWN_ADDR_STRINGS = {'AVE' : 'AVENUE', 'ST': 'STREET', 'S' : 'SOUTH', 'W':'WEST', 'E':'EAST','N':'NORTH', 'BLVD' : 'BOULEVARD', 'TRL' : 'TRAIL', 'STE': 'SITE', 'RD' : 'ROAD', 'PKWY' : 'PARKWAY', 'BLDG' : 'BUILDING', 'PLZ' : 'PLAZA', 'CT' : 'COURT', 'A' : '', 'B' : '', '&' : '', 'Hoyne' : 'Hoyne Avenue', 'PRYOR' : 'Pryor AVENUE', 'DEVON' : 'DEVON AVENUE', 'ROSSELL' : 'ROSSELL AVENUE', 'LN': 'LANE'}

# Typos
TYPO_FIXES = {'COMMERICAL' : 'COMMERCIAL', 'Wasbash' : 'Wabash', 'RIVERSIDEPLZ' : 'RIVERSIDE', 'BROARDWAY' : 'BROADWAY', 'WASTENAW' : 'WASHTENAW', 'WAWR' : 'MAWR', 'GRIFFIN': 'Griffith',  'LAFIN' : 'LAFLIN' }

