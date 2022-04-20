'''

    evaluate.py

    Description: This file contains helper functions for evaluating time series
        predictions.

    Variables:

        None

    Functions:

        evaluate(target, actual, prediction)
        plot_forecast(target, *dfs)
        append_eval_df(model_type, target, actual, prediction, eval_df = None)
        make_static_predictions(target, static_prediction, df_index)

'''

################################################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

################################################################################

def evaluate(target, actual, prediction):
    rmse = round(mean_squared_error(actual[target], prediction[target], squared = False), 0)
    return rmse

################################################################################

def plot_forecast(target, *dfs):
    plt.figure(figsize = (12,4))

    for df in dfs:    
        plt.plot(df[target])

    plt.title(target)
    plt.show()

################################################################################

def append_eval_df(model_type, target, actual, prediction, eval_df = None):
    if eval_df is None:
        eval_df = pd.DataFrame(columns=['model_type', 'target', 'rmse'])

    rmse = evaluate(target, actual, prediction)
    d = {'model_type': [model_type], 'target': [target], 'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)

################################################################################

def make_static_predictions(target, static_prediction, df_index):
    predictions = pd.DataFrame(
        {target : [static_prediction]},
        index = df_index
    )
    return predictions