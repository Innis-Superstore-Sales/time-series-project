'''

    prepare.py

    Description: This file contains functions used for preparing the superstore
        data for exploration and modeling.

    Variables:

        None

    Functions:

        prepare(df)
        clean_columns(df)
        separate_by_region(df)
        separate_by_category(df)
        split_data(df)
        remove_outliers(df, k, col_list)

'''

################################################################################

import pandas as pd

################################################################################

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_columns(df)
    by_week = df.resample('W').sum()
    east_by_week, west_by_week, central_by_week, south_by_week = separate_by_region(df)
    office_supplies_by_week, furniture_by_week, technology_by_week = separate_by_category(df)

    return by_week, east_by_week, west_by_week, central_by_week, south_by_week, office_supplies_by_week, furniture_by_week, technology_by_week

################################################################################

def prepare_remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_columns(df)
    df = remove_outliers(df, 1.5, ['sales'])
    by_week = df.resample('W').sum()
    east_by_week, west_by_week, central_by_week, south_by_week = separate_by_region(df)
    office_supplies_by_week, furniture_by_week, technology_by_week = separate_by_category(df)

    return by_week, east_by_week, west_by_week, central_by_week, south_by_week, office_supplies_by_week, furniture_by_week, technology_by_week

################################################################################

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [column.lower().replace(' ', '_').replace('-','_') for column in df]
    df.order_date = pd.to_datetime(df.order_date)
    df = df.set_index('order_date').sort_index()
    df.drop(columns=['product_id', 'customer_id', 'region_id', 'category_id', 'order_id', 'postal_code', 'ship_date'], inplace=True)
    return df

################################################################################

def separate_by_region(df: pd.DataFrame) -> tuple[pd.DataFrame]:
    supertore_east = df[df.region_name == "East"]
    supertore_west = df[df.region_name == "West"]
    supertore_central = df[df.region_name == "Central"]
    supertore_south = df[df.region_name == "South"]

    east_by_week = supertore_east.resample('W').sum()
    west_by_week = supertore_west.resample('W').sum()
    central_by_week = supertore_central.resample('W').sum()
    south_by_week = supertore_south.resample('W').sum()

    return east_by_week, west_by_week, central_by_week, south_by_week

################################################################################

def separate_by_category(df: pd.DataFrame) -> tuple[pd.DataFrame]:
    office_supplies = df[df.category == 'Office Supplies']
    furniture = df[df.category == 'Furniture']
    technology = df[df.category == 'Technology']

    office_supplies_by_week = office_supplies.resample('W').sum()
    furniture_by_week = furniture.resample('W').sum()
    technology_by_week = technology.resample('W').sum()

    return office_supplies_by_week, furniture_by_week, technology_by_week

################################################################################

def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame]:
    train = df.loc[ : '2015']
    validate = df.loc['2016']
    test = df.loc['2017']

    return train, validate, test

################################################################################

def remove_outliers(df: pd.DataFrame, k: float, col_list: list[str]) -> pd.DataFrame:
    '''
        Remove outliers from a list of columns in a dataframe 
        and return that dataframe.
        
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe containing data from which we want to remove
            outliers.
        
        k: float
            A numeric value that indicates how strict our outlier threshold
            should be. Typically 1.5.

        col_list: list[str]
            A list of columns from which we want to remove outliers.
        
        Returns
        -------
        DataFrame: A pandas dataframe with outliers removed.
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df