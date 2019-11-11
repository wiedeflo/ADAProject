'''
File name: clean_database.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 03/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains methods to clean the database
'''

import pandas as pd
from utils import constants as cst

def clean_socio_economic_df(socio_economic_df):
    '''
    clean the socio-economic dataframe : lower-case area names, drop rows with NaN as community area number, change type of 'community_area_num' to int
    :param df: pandas.DataFrame
    :return: the cleaned socio-economic dataframe
    '''
    # lower-case the area names
    socio_economic_df[cst.AREA_NAME] = socio_economic_df[cst.AREA_NAME].apply(lambda area: area.lower())
    
    # fill NaN with '-1' since the last row has area name "chicago" and area number 'NaN', but we don't want to drop the row
    socio_economic_df[cst.AREA_NUM] = socio_economic_df[cst.AREA_NUM].fillna(-1)
    
    # change 'community_area_num' from float to int
    socio_economic_df[cst.AREA_NUM] = socio_economic_df[cst.AREA_NUM].astype('int')
    
    return socio_economic_df
    
def clean_life_expectancy_df(life_expectancy_df):
    '''
    clean the life-expectancy dataframe : lower-case area names, drop rows with NaN as community area number, change type of 'community_area_num' to int
    :param df: pandas.DataFrame
    :return: the cleaned life-expectancy dataframe
    '''
    
    # lower-case the area names
    life_expectancy_df[cst.AREA_NAME] = life_expectancy_df[cst.AREA_NAME].apply(lambda area: area.lower())
    
    # fill NaN with '-1' since the last row has area name "chicago" and area number 'NaN', but we don't want to drop the row
    life_expectancy_df[cst.AREA_NUM] = life_expectancy_df[cst.AREA_NUM].fillna(-1)
    
    # change 'community_area_num' from float to int
    life_expectancy_df[cst.AREA_NUM] = life_expectancy_df[cst.AREA_NUM].astype('int')
    
    return life_expectancy_df

    
def clean_areas_df(areas_df):
    '''
    clean the areas dataframe : drop duplicated columns, drop columns with the same information, lower-case area names, rename     columns.
    :param df: pandas.DataFrame
    :return: the cleaned areas dataframe
    '''
    
    # notice that the two columns are equal, so we drop the second
    # areas_DF['area_num_1'].equals(areas_DF['area_numbe'])
    areas_df = areas_df.drop('area_numbe', axis=1)
    
    # drop unnecessary columns
    areas_df.loc[:, areas_df.columns != 'geometry'] = drop_columns_with_one_value(areas_df.loc[:, areas_df.columns != 'geometry'])
    
    # rename columns 'area_num_1' and 'community' to more meaningful names
    areas_df = areas_df.rename(columns={'area_num_1': cst.AREA_NUM, 'community': cst.AREA_NAME})
    
    # lower-case the area names
    areas_df[cst.AREA_NAME] = areas_df[cst.AREA_NAME].apply(lambda area: area.lower())
    
    return areas_df
    
    
def drop_columns_with_one_value(df):
    '''
    remove all columns that have only one value in every row (value can be NaN)
    :param df: pandas.DataFrame
    :return: the dataframe with those columns dropped
    '''
    # get columns with unique values
    col_unique_val = df.apply(lambda col: col.nunique())
    # drop those columns (if a column is all-NaN then col_unique_val = 0)
    df_clean = df.drop(col_unique_val[col_unique_val<=1].index, axis=1)
    return df_clean

def drop_all_nan_col(df):
    '''
    remove all columns that have NaN values in every row
    :param df: pandas.DataFrame
    :return: a clean dataframe
    '''
    df_size = len(df)
    nan_cols = []
    for col in df.columns:
        if sum(df[col].isna()) == df_size:
            nan_cols.append(col)
    clean_df = df.drop(nan_cols, axis=1)
    return clean_df


def complete_unknown_lat_lng(df):
    '''
    Some areas have no lat/lng, so we fill them in manually
    :param df: pandas.DataFrame
    :return: a complete dataframe
    '''
    # if there are no NaN values, the df is already complete
    if df['lat'].isna().sum() + df['lng'].isna().sum() == 0:
        return df
    else:
        # We correct it by hand :
        lat_lng_idx_area = {}
            
        area_name = 'Montclaire'
        lat_lng_idx_area[area_name] = {'lat':constants.MONTCLAIRE_AREA_LAT, 'lng':constants.MONTCLAIRE_AREA_LNG, 'idx': df.index[df[cst.AREA_NAME] == area_name].values[0]}
        
        area_name = 'Washington Height'
        lat_lng_idx_area[area_name] = {'lat':constants.WASHINGTON_HEIGHT_AREA_LAT, 'lng':constants.WASHINGTON_HEIGHT_AREA_LNG, 'idx': df.index[df[cst.AREA_NAME] == area_name].values[0]}
        

        df.loc[lat_lng_idx_area['Montclaire']['idx'], 'lat'] = lat_lng_idx_area['Montclaire']['lat']
        df.loc[lat_lng_idx_area['Montclaire']['idx'], 'lng'] = lat_lng_idx_area['Montclaire']['lng']
        df.loc[lat_lng_idx_area['Washington Height']['idx'], 'lat'] = lat_lng_idx_area['Washington Height']['lat']
        df.loc[lat_lng_idx_area['Washington Height']['idx'], 'lng'] = lat_lng_idx_area['Washington Height']['lng']
    
    return df