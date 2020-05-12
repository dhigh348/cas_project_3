import pandas as pd
from data_analyzer import DataAnalyzer
import numpy as np 

class Economy:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def edit_data(self, data, new_cols):
        # edit the data -> filter by year, set index column and get rid of na values
        data.set_index('DATE', inplace=True)
        data = data.filter(like='2018', axis=0)
        data.rename(columns=new_cols, inplace=True)
        return data

    def load_data(self, path, wages):
        data = pd.read_csv(path)
        if wages:
            data = self.edit_data(data=data, new_cols={data.columns[-1]: 'wages'})
        else:
            data = self.edit_data(data=data, new_cols={})
        return data

    def make_graph(self, data):
        analyzer = DataAnalyzer(data)
        data_norm = analyzer.normalize_dataframe()
        analyzer.plot_data(data_norm, 'month', 'stuff', 'title stuff', '../data/figures/local_eco.png')
