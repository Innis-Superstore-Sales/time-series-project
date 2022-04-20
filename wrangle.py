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
from prepare import prepare

################################################################################

def wrangle():
    return prepare(AcquireSuperstore().get_data())