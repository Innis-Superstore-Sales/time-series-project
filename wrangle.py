'''

    wrangle.py

    Description: This file contains functions used for acquiring and preparing 
        the superstore data.

    Variables:

        None

    Functions:

        wrangle()
        wrangle_remove_outliers()

'''

################################################################################

from acquire import AcquireSuperstore
from prepare import *

################################################################################

def wrangle():
    return prepare(AcquireSuperstore().get_data())

################################################################################

def wrangle_remove_outliers():
    return prepare_remove_outliers(AcquireSuperstore().get_data())