'''

    prepare.py

    Description: Description

    Variables:

        Variable

    Functions:

        Function

'''

################################################################################

import pandas as pd

################################################################################

def prepare(df):
    df.columns = [column.lower().replace(' ', '_').replace('-','_') for column in df]
    df.order_date = pd.to_datetime(df.order_date)
    df = df.set_index('order_date').sort_index()
    df.drop(columns=['product_id', 'customer_id', 'region_id', 'category_id', 'order_id', 'postal_code', 'ship_date'], inplace=True)
    by_week = df.resample('W').sum()

    supertore_east = df[df.region_name == "East"]
    supertore_west = df[df.region_name == "West"]
    supertore_central = df[df.region_name == "Central"]
    supertore_south = df[df.region_name == "South"]

    east_by_week = supertore_east.resample('W').sum()
    west_by_week = supertore_west.resample('W').sum()
    central_by_week = supertore_central.resample('W').sum()
    south_by_week = supertore_south.resample('W').sum()

    return by_week, east_by_week, west_by_week, central_by_week, south_by_week