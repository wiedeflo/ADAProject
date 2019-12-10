'''
File name: constants.py
Date created: 03/11/2019
Date last modified: 24/11/2019
Python Version: 3.7.4
Contains constants on the database file paths, columns names, Chicago addresses or locations, etc
'''
###########################################################################################################
################################################ DATABASES ################################################
###########################################################################################################

# Data Folder
DATA_PATH = '../data/'
MAPS_PATH = '../website/maps/'

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

# Unknown locations data path
UNKNOWN_LOC_PATH = DATA_PATH + 'unknown_locations_df.pkl'

FOOD_INSPECTIONS_AREA_PICKLE = DATA_PATH + 'food_inspections_area_pickle.pkl'

###########################################################################################################
######################################## LNG/LAT FROM CHICAGO AREA ########################################
###########################################################################################################

# Chicago location 
CHICAGO_LOCATION = [41.8333925,-87.7121486]
CHICAGO_MIN_LAT = 41.625364
CHICAGO_MAX_LAT = 42.099612
CHICAGO_MIN_LNG = -88.000493
CHICAGO_MAX_LNG = -87.463580

# Web scraping
LAT_LNG_HTML_POSITION_START = 'window.APP_INITIALIZATION_STATE=[[['
LAT_LNG_HTML_POSITION_STOP = ']'
CHICAGO_AREA_URL = 'https://www.google.com/maps/place/%s,+Chicago,+IL,+USA'
CHICAGO_ADDRESS = "Chicago, Illinois, United States"

# Montclaire and Washington areas
MONTCLAIRE_AREA_LAT = 41.929681
MONTCLAIRE_AREA_LNG = -87.799306
WASHINGTON_HEIGHT_AREA_LAT = 41.718415
WASHINGTON_HEIGHT_AREA_LNG = -87.642884

# Geopy lib
GEOPY_USER_AGENT = "not sure what to write : TODO"
GEOPY_TIMEOUT = 10

# Strings that we manually replace as they contain insufficient information
UNKNOWN_ADDR_SUBSTRINGS = {'/SIDE DRIVE' : '', "O'HARE FIELD" : "O'HARE", 'SITE 322' : '', 'Rockwell AVENUE' : 'Rockwell Street', 'Doty' : 'Doty AVENUE', '2104AB-2108A SOUTH ARCHER AVENUE' : '2108 South Archer Avenue', 'WEST WEST' : 'WEST', 'DELANO WEST COURT': 'DELANO Court', 'DELANO EAST COURT': 'DELANO Court', '108 WEST PARK' : '108 West Park Avenue, Elmhurst', '4934 SOUTH Wabash BUILDING' : '4934 South Wabash Avenue', '3901 SOUTH DR MARTIN LUTHER KING JR' : '3901 SOUTH DR MARTIN LUTHER KING Junior Drive', '8306 SOUTH LAWRENCE AVENUE' : '8306 WEST LAWRENCE AVENUE', '1332 WEST DRIVING PARK ROAD BSMT': '1332 West Irving Park Road', '2300 NORTH Childrens Plaza PLAZA BUILDING' : '720 West Fullerton Parkway', '3107 SOUTH 71st STREET BSMT' : '3107 West 71st Street', '2920 SOUTH WENWORTH SITE 2' : '2920 South Wentworth Avenue', '6601 MARTIN FRANCE' : '6601 MARTIN FRANCE CIRCLE', '13946 SOUTH CHIPPEWA' : '13946 SOUTH CHIPPEWA AVENUE', '2217 WEST CRYSTAL STREET APT 2' : '2217 WEST CRYSTAL STREET', '1413 SOUTH 11 TH AVENUE':'1413 SOUTH 11TH AVENUE', '4500 SOUTH WOODS STREET' : '4500 SOUTH WOOD STREET', '425 EAST MC FETRIDGE BUILDING':'425 East McFetridge Drive', '4000 NORTH OHARE AIRPORT':'4000 NORTH OHARE', '3455-3459 SOUTH OGDEN AVENUE' : '3455 Ogden Avenue', '7911 SOUTH WOODS BUILDING' : '7911 South Wood Street', '3455-3459 SOUTH OGDEN AVENUE' : '3459 West Ogden Avenue', '6237 SOUTH HALSTED PARKWAY' : '6237 SOUTH UNION AVENUE', 'SOUTH Western' : 'South Western Avenue', 'EAST WATER STREET' : 'East South Water Street', '912 NORTH WALTON STREET' : '912 NORTH STATE STREET', '743 WEST DRIVING PARK ROAD' : '743 WEST IRVING PARK ROAD', '7600 SOUTH CHICAGO AVE' : '7600 SOUTH SOUTH CHICAGO AVE', 'SOUTH WESTERN' : 'South Western Avenue', '(St. Maurice)' : ''}

# Known Abbreviations and some minor address fixed
KNOWN_ADDR_STRINGS = {'AVE' : 'AVENUE', 'ST': 'STREET', 'S' : 'SOUTH', 'W':'WEST', 'E':'EAST','N':'NORTH', 'BLVD' : 'BOULEVARD', 'TRL' : 'TRAIL', 'STE': 'SITE', 'RD' : 'ROAD', 'PKWY' : 'PARKWAY', 'BLDG' : 'BUILDING', 'PLZ' : 'PLAZA', 'CT' : 'COURT', 'A' : '', 'B' : '', '&' : '', 'Hoyne' : 'Hoyne Avenue', 'Wabash':'Wabash Avenue', 'Pryor' : 'Pryor AVENUE', 'DEVON' : 'DEVON AVENUE', 'ROSSELL' : 'ROSSELL AVENUE', 'LN': 'LANE'}

# Typos
TYPO_FIXES = {'COMMERICAL' : 'COMMERCIAL', 'Wasbash' : 'Wabash', 'RIVERSIDEPLZ' : 'RIVERSIDE', 'BROARDWAY' : 'BROADWAY', 'WASTENAW' : 'WASHTENAW', 'WAWR' : 'MAWR', 'GRIFFIN': 'Griffith',  'LAFIN' : 'LAFLIN', 'CULYER' : 'CUYLER' }

