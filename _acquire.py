'''

    acquire.py

    Description: This file contains an Acquire class which can be used as a
        parent class for data acquisition. Simply inherit the class and 
        set the file_name. Then override the read_from_source method with 
        the code necessary to read the data from the source and you're all 
        set.

    Class:

        Acquire

    Class Fields:

        file_name

    Class Methods:

        __init__(self, file_name, database_name, sql)
        get_data(self, use_cache = True, cache_data = True)
        read_from_source(self)

'''

################################################################################

import os
import pandas as pd

################################################################################

class Acquire:
    '''
        A data acquisition class that can be used for acquiring data and cacheing it in 
        a csv file.

        If a .csv file does not exist in the directory you must override the 
        read_from_source method, otherwise an exception will be raised.
        
        Instance Methods
        ----------------
        __init__: Returns None
        get_data: Returns DataFrame
        read_from_source: Returns DataFrame
    '''

    ################################################################################

    def __init__(self, file_name: str = '') -> None:
        '''
            Parameters
            ----------
            file_name: str
                A .csv file name for cacheing data for quicker access.
        '''

        self.file_name = file_name

    ################################################################################

    def get_data(self, use_cache: bool = True, cache_data: bool = True, output = True) -> pd.DataFrame:
        '''
            Return a dataframe containing data from the database defined by 
            self.database_name.

            If a .csv file containing the data does not already exist the data 
            will be cached in a .csv file inside the current working directory. 
            Otherwise, the data will be read from the .csv file. The filename is 
            defined by self.file_name.

            Parameters
            ----------
            use_cache: bool, optional
                If True the dataset will be retrieved from a csv file if one
                exists, otherwise, it will be retrieved from the MySQL database. 
                If False the dataset will be retrieved from the MySQL database
                even if the csv file exists.

            cache_data: bool, optional
                If True the dataset will be cached in a csv file.

            Returns
            -------
            DataFrame: A Pandas DataFrame containing data from the source provided.
        '''

        # If the file is cached, read from the .csv file
        if os.path.exists(self.file_name) and use_cache:
            if output: print('Reading from .csv file.')
            return pd.read_csv(self.file_name)
        
        # Otherwise read from the mysql database
        else:
            if output: print('Reading from source.')
            df = self.read_from_source()

            # Cache the data in a .csv file, if that is what we want
            if cache_data:
                if output: print('Cacheing data.')
                df.to_csv(self.file_name, index = False)

            return df

    ################################################################################

    def read_from_source(self):
        '''
            This method must be implemented in a child class otherwise a 
            NotImplementedError will be raised.
        '''

        raise NotImplementedError('''
            The read_from_source method has not been implemented.
            This method must be implemented in a child class in order
            to read data from the source. Otherwise, a .csv file 
            containing the required data must be manually downloaded.
        ''')