import yfinance as yf
import numpy as np 
import pandas as pd 

# Comparing stocks at a local level
class CompareLocal:

    # initializing the class
    def __init__(self, sectors, start_date, end_date):
        self.data = pd.DataFrame()
        self.sectors = sectors
        self.start_date = start_date
        self.end_date = end_date

    # getting the ticker data from each of the stocks
    def get_ticker_data(self, stock):
        stock_ticker = yf.Ticker(stock)
        stcok_data = stock_ticker.history('1y', 
                                          interval='1d', 
                                          start=self.start_date, 
                                          end=self.end_date)
        return stcok_data['Close']

    # getting data from the stock
    def get_data(self):
        for stock in self.sectors:
            self.data[stock] = self.get_ticker_data(stock)