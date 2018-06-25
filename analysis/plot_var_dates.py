# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:24:16 2018

@author: rjo40
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import numpy as np
from get_df import get_df


def plot_dates(x, y, labels):
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    ax1.scatter(x,y)


def main():
    global df
    df = get_df()
    
    variables = list(df)
    variables.remove('date')
    x = df['date'][0]
    for variable in variables:
        labels = ['date', variable]
        y = df[variable]
        plot_dates(x,y,labels)
    
    
if __name__ == '__main__':
    main()
    