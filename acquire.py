'''

    acquire.py

    Description: This file contains the data acquisition code for acquiring the 
        superstore data from data.codeup.com. The example below demonstrates how 
        to acquire the data.

        Example:
            df = AcquireSuperstore().get_data()

    Class Fields:

        file_name
        database_name
        sql

    Class Methods:

        __init__(self)
        read_from_source(self)

    Inherited Methods:

        get_data(self, use_cache = True, cache_data = True)

'''

################################################################################

import pandas as pd
from get_db_url import get_db_url

from _acquire import Acquire

################################################################################

class AcquireSuperstore(Acquire):

    ################################################################################

    def __init__(self):
        self.file_name = 'superstore.csv'
        self.database_name = 'superstore_db'
        self.sql = '''
        SELECT
            orders.*,
            Category,
            `Sub-Category`,
            `Customer Name`,
            `Product Name`,
            `Region Name`
        FROM orders
        JOIN categories USING (`Category ID`)
        JOIN customers USING (`Customer ID`)
        JOIN products USING (`Product ID`)
        JOIN regions USING (`Region ID`);
        '''

    ################################################################################
        
    def read_from_source(self):
        return pd.read_sql(self.sql, get_db_url(self.database_name))