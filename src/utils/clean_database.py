'''
File name: clean_database.py
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 03/11/2019
Date last modified: ...
Python Version: 3.7.4
Contains methods to clean the database
'''

import pandas as pd

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
        lat_lng_idx_area[area_name] = {'lat':constants.MONTCLAIRE_AREA_LAT, 'lng':constants.MONTCLAIRE_AREA_LNG, 'idx': df.index[df['community_area_name'] == area_name].values[0]}
        
        area_name = 'Washington Height'
        lat_lng_idx_area[area_name] = {'lat':constants.WASHINGTON_HEIGHT_AREA_LAT, 'lng':constants.WASHINGTON_HEIGHT_AREA_LNG, 'idx': df.index[df['community_area_name'] == area_name].values[0]}
        

        df.loc[lat_lng_idx_area['Montclaire']['idx'], 'lat'] = lat_lng_idx_area['Montclaire']['lat']
        df.loc[lat_lng_idx_area['Montclaire']['idx'], 'lng'] = lat_lng_idx_area['Montclaire']['lng']
        df.loc[lat_lng_idx_area['Washington Height']['idx'], 'lat'] = lat_lng_idx_area['Washington Height']['lat']
        df.loc[lat_lng_idx_area['Washington Height']['idx'], 'lng'] = lat_lng_idx_area['Washington Height']['lng']
    
    return df