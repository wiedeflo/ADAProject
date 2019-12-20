'''
File name: predictions_helpers.py
Date created: 18/12/2019
Date last modified: 20/12/2019
Python Version: 3.7.4
Contains helpers methods for the last part of the notebook.
'''

import re
import numpy as np
from datetime import datetime


def risk_to_num(x):
    """
    Get a number from a risk : Risk 3 -> 1, Risk 2 -> 2, Risk 1 -> 3
    :param x: string
    :return: integer
    """
    if x == 'Risk 3 (Low)':
        return 1
    if x == 'Risk 2 (Medium)':
        return 2
    if x == 'Risk 1 (High)':
        return 3
    if x == 'All':
        return 2
    else:
        return x
    
def inspected_after_2018(l):
    """
    Return true if input is after 2018
    :param x: pandas.DataFrame
    :return: boolean
    """
    for e in l:
        e = datetime.strptime(e[:10], '%Y-%m-%d')
        if e > datetime(year = 2018, month = 4, day = 1):
            return True
    return False

def n_inspections_before_2018(l):
    """
    Return the number of inspections before 2018
    :param x: pandas.DataFrame
    :return: integer 
    """
    n = 0
    for e in l:
        e = datetime.strptime(e[:10], '%Y-%m-%d')
        if e < datetime(year = 2018, month = 4, day = 1):
            n+=1
    return n

def results_to_number(result_l):
    """
    Return the mean of an array consisting of pass (2), pass with conditions (1) and fail (0)
    :param x: pandas.DataFrame
    :return: numpy.float 
    """
    l_no = []
    for e in result_l:
        if e == 'Pass':
            l_no.append(2)
        if e == 'Pass w/ Conditions':
            l_no.append(1)
        if e == 'Fail':
             l_no.append(0)
    return np.mean(l_no)

def int_of_x(x):
    """
    Convert x to integer
    :param x: object
    :return: integer 
    """
    try:
        return int(x)

    except Exeption:
        return -1