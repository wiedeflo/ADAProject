import re
import numpy as np
from datetime import datetime


def risk_to_num(x):
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
    
#based ob the performance between 2010 - 2017, predict if there is an inspection in 2019
def inspected_after_2018(l):
    for e in l:
        e = datetime.strptime(e[:10], '%Y-%m-%d')
        if e > datetime(year = 2018, month = 4, day = 1):
            return True
    return False
def n_inspections_before_2018(l):
    n = 0
    for e in l:
        e = datetime.strptime(e[:10], '%Y-%m-%d')
        if e < datetime(year = 2018, month = 4, day = 1):
            n+=1
    return n

def results_to_number(result_l):
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
    try:
        return int(x)

    except Exeption:
        return -1