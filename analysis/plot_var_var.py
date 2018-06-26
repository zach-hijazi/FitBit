import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import numpy as np
from get_df import get_df

def plot_dates(x, y, var_pair):
    """plot variable of interest versus date
    """
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    ax1.scatter(x,y)
    fig1.savefig('var_var_plots2/'+str(var_pair[0])+str(var_pair[1])+'.tiff', dpi=300)
    plt.close(fig1)
    print('plotted' + str(var_pair))


def main():
    """get dataframe from raw data, then plot all variables
    versus all other variables and determine the correlations
    """
    #get dataframe from raw data
    df = get_df()

    #get list of variables to plot versus data
    variables = list(df)
    variables.remove('date')

    var_pairs = [(var1, var2) for var1 in variables for var2 in variables if variables.index(var2) > variables.index(var1)]
    print(len(var_pairs))
    #get x and y, then recursively plot all variables
    for var_pair in var_pairs:

        x = df[var_pair[0]]
        y = df[var_pair[1]]

        plot_dates(x,y,var_pair)


if __name__ == '__main__':
    main()
