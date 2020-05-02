import pandas as pd
from data_analyzer import DataAnalyzer

class Economy:

    def __init__(self, start, end, unemployment_path, income_path):
        self.start = start
        self.end = end 
        self.unemployment_path = unemployment_path
        self.income_path = income_path

    # getting the data for the 
    def get_data(self):
        self.unemployment_data = pd.read_csv(self.unemployment_path)
        self.income_data = pd.read_csv(self.income_path)

    # printing the data
    def print_data(self, xlabel, ylabel, title, fig_path):
        income_analysis = DataAnalyzer(self.income_path)
        income_analysis.plot_data(self.income_data, xlabel, ylabel, title, fig_path)

        unemployment_analysis = DataAnalyzer(self.unemployment_data)
        unemployment_analysis.plot_data(self.unemployment_data, xlabel, ylabel, title, fig_path)