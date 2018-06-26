# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:06:50 2018

@author: rjo40
"""

import pandas as pd
from os import listdir

def get_df():
    """return a DataFrame that is generated from the Fitbit website and
    contains the user's daily activity data (sleep and exersize) that will be
    used for further analysis
    """

    #generate sleep and activity dataframe from raw data files
    files = listdir('../data')
    df = pd.DataFrame()
    df_sleep = pd.DataFrame()
    for file in files:
        tmp_df = pd.read_csv('../data/'+file, skiprows = 1)
        if file[:3] == 'act':
            df = df.append(tmp_df, ignore_index = True)
        else:
            df_sleep = df_sleep.append(tmp_df, ignore_index = True)

    #separate sleep date and time into seperate columns
    df_sleep['Date'] = df_sleep['Start Time'].apply(lambda row: row[:10])
    df_sleep['Start Time'] = df_sleep['Start Time'].apply(lambda row: row[11:])
    df_sleep['End Time'] = df_sleep['End Time'].apply(lambda row: row[11:])

    #combine sleep and activity dataframe by common date
    col = ['Date']
    df = df.join(df_sleep.set_index(col), col)

    #clean-up and format dataframe
    df = df.rename(columns = lambda x: x.replace(' ', '_').lower())
    df = df[df.distance != 0.0]
    df = df.dropna()
    return df
