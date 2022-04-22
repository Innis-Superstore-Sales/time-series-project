'''

    explore.py

    Description: This file contains functions used for creating visualizations and performing
        stats tests in the final report notebook for the superstore time series project.

    Variables:

        None

    Functions:

        plot_discount_and_profit()

'''

################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from acquire import AcquireSuperstore
from prepare import *

################################################################################

def plot_discount_and_profit():
    superstore_raw = clean_columns(AcquireSuperstore().get_data())

    plt.figure(figsize = (14, 6))

    ax = sns.barplot(
        data = superstore_raw,
        x = 'discount',
        y = 'profit',
        ci = None,
        palette = ['#005697']
    )

    ax.set_xticklabels(['0%', '10%', '15%', '20%', '30%', '32%', '40%', '45%', '50%', '60%', '70%', '80%'])
    plt.xlabel('Discount')

    ax.set_yticklabels([f'${tick:,.0f}' for tick in ax.get_yticks()])
    plt.ylabel('Profit')

    plt.title('Large discounts are leading to greater losses\n***\nAverage profit for various discount rates')

    plt.show()