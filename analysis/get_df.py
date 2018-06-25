# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:06:50 2018

@author: rjo40
"""

import pandas as pd 
from os import listdir

def get_df():
    global df
    def get_col_data(parameter, s):
        """
        pull out df values from file names 
        """
        return s[s.index(parameter)+len(parameter + '_'): s.index('_', s.index(parameter)+len(parameter + '_'))]
    
    #generate df from raw data files 
    global files
    files = listdir('../data')
    df = pd.DataFrame()
    df_sleep = pd.DataFrame()
    for file in files:
        tmp_df = pd.read_csv('../data/'+file, skiprows = 1)
        if file[:3] == 'act':
            df = df.append(tmp_df, ignore_index = True)
        else:
            df_sleep = df_sleep.append(tmp_df, ignore_index = True)
    df_sleep['Date'] = df_sleep['Start Time'].apply(lambda row: row[:10])
    df_sleep['Start Time'] = df_sleep['Start Time'].apply(lambda row: row[11:])
    df_sleep['End Time'] = df_sleep['End Time'].apply(lambda row: row[11:])
    col = ['Date']
    df = df.join(df_sleep.set_index(col), col)
    df = df.rename(columns = lambda x: x.replace(' ', '_').lower())
    df = df[df.distance != 0.0]
    df = df.dropna()
    return df
