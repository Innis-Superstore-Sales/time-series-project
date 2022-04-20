'''

    model.py

    Description: Description

    Variables:

        Variable

    Functions:

        Function

'''

################################################################################

import pandas as pd

import statsmodels.api as sm
from statsmodels.tsa.api import Holt
from prophet import Prophet

from evaluate import *

################################################################################

def establish_baseline(train, validate):
    forecast_values = {
        'Last Observed Value' : round(train.sales[-1], 2),
        'Simple Average' : round(train.sales.mean(), 2)
    }

    periods = [4, 12, 26, 52]
    for period in periods:
        forecast_values[f'Moving Average {period} Weeks'] = round(train.sales.rolling(period).mean()[-1], 2)

    predictions = {}
    for key, value in forecast_values.items():
        predictions[key] = make_static_predictions('sales', value, validate.index)

    eval_df = None
    for key, prediction in predictions.items():
        eval_df = append_eval_df(key, 'sales', validate, prediction, eval_df)

    return eval_df[eval_df.rmse == eval_df.rmse.min()]