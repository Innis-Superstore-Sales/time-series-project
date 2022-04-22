'''

    explore.py

    Description: This file contains functions used for creating visualizations and performing
        stats tests in the final report notebook for the superstore time series project.

    Variables:

        background_color
        palette

    Functions:

        plot_discount_and_profit()

'''

################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from acquire import AcquireSuperstore
from prepare import *

################################################################################

background_color = '#fcf6f6'
palette = ['#005697']

################################################################################

def plot_discount_and_profit():
    superstore_raw = clean_columns(AcquireSuperstore().get_data())

    plt.figure(figsize = (14, 6))

    ax = sns.barplot(
        data = remove_outliers(superstore_raw, 3.0, ['profit']),
        x = 'discount',
        y = 'profit',
        ci = None,
        palette = palette
    )

    ax.set_xticklabels(['0%', '10%', '15%', '20%', '30%', '32%', '40%', '50%', '60%', '70%', '80%'])
    plt.xlabel('Discount')

    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    plt.ylabel('Profit')

    plt.title('Average profit for various discount rates')

    plt.show()

################################################################################

def seasonal_plot_average_sales(df):
    ax = df.groupby([df.index.year, df.index.month]).sales.mean().unstack(0).plot(figsize = (14, 6))
    plt.title('Average Sales by Year')

    plt.axvline(x = 8, linestyle = '--')

    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    plt.ylabel('Average Sales')

    plt.xticks(ticks = [x for x in range(1, 13)], labels = [month[ : 3] for month in df.index.month_name().unique()])
    plt.xlabel('Month')

    # Reorder labels in legend and add a title.
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(
        reversed(handles),
        reversed(labels),
        title = 'Year'
    )

    plt.show()

################################################################################

def plot_average_monthly_sales(df):
    ax = df.groupby(df.index.month).sales.mean().plot(kind = 'bar', colormap = 'Blues_r', figsize = (14, 6))

    ax.tick_params('x', rotation=0)
    plt.xticks(ticks = [x for x in range(12)], labels = [month[ : 3] for month in df.index.month_name().unique()])

    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])

    ax.set(title='Average Monthly Sales', xlabel='Month', ylabel='Average Sales')

    plt.show()

################################################################################

def run_stats_test_on_average_monthly_sales(df):
    alpha = 0.05
    first_half = df.index.month < 6.5
    second_half = df.index.month > 6.5
    
    _, p = stats.ttest_ind(df[first_half].sales, df[second_half].sales, equal_var = False)

    if p < alpha:
        print('Reject H0')
    else:
        print('Fail to reject H0')

################################################################################

def plot_quarterly_sales(df):
    ax = df.sales.resample('3M').mean().plot(figsize = (14, 6))
    plt.title('Average Quarterly Sales')

    plt.xlabel('Year')

    plt.ylabel('Average Sales')
    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])

    plt.show()

################################################################################

def plot_quarterly_profit(df):
    ax = df.profit.resample('3M').mean().plot(figsize = (14, 6))
    plt.title('Average Quarterly Profit')

    plt.xlabel('Year')

    plt.ylabel('Average Profit')
    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])

    plt.show()

################################################################################

def run_stats_test_on_yearly_sales(df):
    alpha = 0.05
    year_2014 = df.index.year == 2014
    year_2017 = df.index.year == 2017

    _, p = stats.ttest_ind(df[year_2014].sales, df[year_2017].sales, equal_var = True)

    if p < alpha:
        print('Reject H0')
    else:
        print('Fail to reject H0')