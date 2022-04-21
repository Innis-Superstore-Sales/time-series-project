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

def establish_baseline(train, validate, periods):
    forecast_values = {
        'Last Observed Value' : round(train.sales[-1], 2),
        'Simple Average' : round(train.sales.mean(), 2)
    }

    for period in periods:
        forecast_values[f'Moving Average {period} Weeks'] = round(train.sales.rolling(period).mean()[-1], 2)

    predictions = {}
    for key, value in forecast_values.items():
        predictions[key] = make_static_predictions('sales', value, validate.index)

    eval_df = None
    for key, prediction in predictions.items():
        eval_df = append_eval_df(key, 'sales', validate, prediction, eval_df)

    return eval_df[eval_df.rmse == eval_df.rmse.min()]

################################################################################

def create_ensemble_predictions(trains, validates, target, strategy):
    predictions = []

    for train, validate in zip(trains, validates):
        predictions.append(strategy(target, train, validate))

    df = predictions[0]
    for prediction in predictions[1 : ]:
        df = df + prediction
    return df

################################################################################

def simple_average_model(target, train, validate):
    return make_static_predictions(target, train[target].mean(), validate.index)

################################################################################

def holt_model(target, train, validate):
    model = Holt(train[target], damped_trend = True)
    model = model.fit()
    predictions =  model.predict(
        start = validate.index[0],
        end = validate.index[-1]
    )
    return pd.DataFrame(predictions, columns = [target], index = predictions.index)

################################################################################

def prophet_model(target, train, validate, period = 365):
    model = Prophet()
    model.fit(pd.DataFrame({
        'ds' : train.index,
        'y' : train[target]
    }))

    future = model.make_future_dataframe(period)
    results = model.predict(future)
    predictions = results[['ds', 'yhat']].set_index('ds')
    predictions.columns = [target]
    return predictions.resample('M').mean()

################################################################################

def previous_cycle_model(target, train, validate):
    predictions = train.loc['2015'] + train.diff(12).mean()
    predictions.index = validate.index
    return predictions