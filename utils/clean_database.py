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