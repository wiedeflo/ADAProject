'''
File name: load_datasets.ipynb
Author: ..., Mohamed Ndoye, Raphael Strebel
Date created: 03/11/2018
Date last modified: ...
Python Version: 3.7.4
'''

import pandas as pd
from sodapy import Socrata

# copied from : https://www.sustainabilist.com/blog/chicago-data-analysis-a-internship-project

def load_chicago_df(inspection_DB_identifer:str, limit:int, chicago_url:str):
    '''
    return a dataframe loaded from the website 'data.cityofchicago.org'
    :param inspection_DB_identifer: string
    :param limit: int
    :param chicago_url: string
    :return: pandas.DataFrame
    '''
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata(chicago_url, None)

    # First 50000 results, received as JSON & returned as dict
    # Columns converted to snake case, special chars removed,
    # dates and location formatted
    chicago_DB_records = client.get(inspection_DB_identifer, limit=limit)

    # Convert to pandas DataFrame
    chicago_DF = pd.DataFrame.from_records(chicago_DB_records)
    return chicago_DF