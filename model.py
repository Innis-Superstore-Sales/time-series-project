'''

    model.py

    Description: This file contains functions used for producing forecasting
        models for the superstore time series project

    Variables:

        None

    Functions:

        establish_baseline(train, validate, periods)
        create_ensemble_predictions(trains, validates, target, strategy)
        simple_average_model(target, train, validate)
        holt_model(target, train, validate)
        prophet_model(target, train, validate, period = 365)
        previous_cycle_model(target, train, validate)

'''

################################################################################

import os
import pandas as pd

import statsmodels.api as sm
from statsmodels.tsa.api import Holt
from prophet import Prophet

from evaluate import *

################################################################################

def create_models(target, train, validate, eval_df):
    predictions = holt_model(target, train, validate)
    eval_df = append_eval_df("Holt's Linear Trend", target, validate, predictions, eval_df)

    predictions = prophet_model(target, train, validate)
    eval_df = append_eval_df("Prophet", target, validate, predictions.loc['2016'], eval_df)

    predictions = previous_cycle_model(target, train, validate)
    eval_df = append_eval_df("Previous Cycle", target, validate, predictions, eval_df)

    return eval_df

################################################################################

def establish_baseline(train: pd.DataFrame, validate: pd.DataFrame, periods: list[int]) -> pd.DataFrame:
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
    }), verbose = False)

    future = model.make_future_dataframe(period)
    results = model.predict(future)
    predictions = results[['ds', 'yhat']].set_index('ds')
    predictions.columns = [target]
    return predictions.resample('W').mean()

################################################################################

def previous_cycle_model(target, train, validate, period = 52):
    predictions = train.loc['2015'] + train.diff(period).mean()
    predictions.index = validate.index
    return predictions

################################################################################

# from https://stackoverflow.com/questions/11130156/suppress-stdout-stderr-print-from-python-functions
class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).

    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])