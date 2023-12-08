import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error



# Loads data into a variable
# Data must be stored in a folder called DATA that is one level above the current working directory
# Stock data must be in a file caled ticker_Data.csv (i.e. AAPL_Data.csv)
def load_dataset(stockname):
    filepath = '../DATA/' + stockname + '_Data.csv'
    data = remove_dollar_signs(pd.read_csv(filepath, sep=',', index_col='Date', parse_dates=['Date']))
    return data[::-1]

# Removes dollar signs and converts strings to numbers for the provided data
# Takes in the data taken from load_dataset() and returns updated data in the correct format
def remove_dollar_signs(data):
    data["Close/Last"] = data["Close/Last"].replace({'\$': ''}, regex=True).apply(pd.to_numeric, errors='ignore')
    data["Open"] = data["Open"].replace({'\$': ''}, regex=True).apply(pd.to_numeric, errors='ignore')
    data["High"] = data["High"].replace({'\$': ''}, regex=True).apply(pd.to_numeric, errors='ignore')
    data["Low"] = data["Low"].replace({'\$': ''}, regex=True).apply(pd.to_numeric, errors='ignore')
    return data

#TODO Build the code to make graphs for stationarity, seasonality and autocorrelation

#TODO Build the model to predict each of the stocks prices

#TODO Plot the stock price predictions from the model

