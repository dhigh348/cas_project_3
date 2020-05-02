from compare_local import CompareLocal
from data_analyzer import DataAnalyzer
from local_economy import Economy
import pandas as pd

# checking if the data contains na values
def check_data(data):
    if data.isna().values.any():
        return data.dropna()
    else:
        return data 

# function to make the california data
def make_cali_data():
    cali_stock = CompareLocal(sectors, '2018-01-01', '2019-01-01')
    cali_stock.get_data()
    print(cali_stock.data.head())
    return cali_stock

# function to analyze and print californias data graphs
def make_graphs(stock_data):
    da = DataAnalyzer(stock_data.data)
    data = da.normalize_dataframe()

    # making the figures
    # norms
    da.plot_data(data,
                 'months', 
                 'stock data',
                 'Test',
                 '../data/figures/all.png')
    # mean of the norms             
    da.plot_data(data.mean(axis=1),
                 'months', 
                 'stock data mean', 
                 'Price Means', 
                 '../data/figures/mean.png') 

# getting data of stocks over time interval of Hurrcane Katrina
def make_la_data():
    lousianna = CompareLocal(sectors, '2005-01-01', '2006-01-01')
    lousianna.get_data()
    print(lousianna.data.head())
    return lousianna

# making figures from the stock data over hurricane katrina timeline
def make_la_figs(stock_data):
    da = DataAnalyzer(stock_data)
    data = da.normalize_dataframe()

    # making the figures
    # normalized data
    da.plot_data(data,
                 'months', 
                 'stock data', 
                 'Stock Data',
                 '../data/figures/no_all.png')
    # mean of normalized data
    da.plot_data(data.mean(axis=1),
                 'months', 
                 'stock data', 
                 'Stock Data',
                 '../data/figures/no_mean.png')

# main function to run the program
def main():
    # making california data and making figures
    cali_stock = make_cali_data()
    make_graphs(cali_stock)

    # check california economy
    cali_eco = Economy(start='2018',
                       end='2019',
                       unemployment_path='../data/ca_unemp.csv',
                       income_path='../data/cali_hourly_wages.csv')
    cali_eco.get_data()
    # cali_eco.print_data(xlabel='months', 
    #                     ylabel='data',
    #                     title='prices',
    #                     fig_path='../data/figures/income.png')

    # making NO data and making figures
    # loisianna_stocks = make_la_data()
    # make_la_figs(loisianna_stocks)

# running the function
if __name__ == "__main__":
    sectors = {'XLE': 'XOM', 
           'XLB': 'ECL',
           'XLI': 'LMT',
           'XLY': 'AMZN',
           'XLP': 'WMT',
           'XLV': 'JNJ',
           'XLF': 'JPM',
           'XLK': 'INTC',
           'XTL': 'AAPL',
           'XLU': 'DUK',
           'XLRE': 'SPG'}
    
    # running the program 
    main()

    