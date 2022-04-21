'''

    wrangle.py

    Description: Description

    Variables:

        Variable

    Functions:

        Function

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