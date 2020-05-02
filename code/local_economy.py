import pandas as pd
from data_analyzer import DataAnalyzer

# economy class
class Economy:

    # initializing the economy class
    def __init__(self, start, end, unemployment_path, income_path):
        self.start = start
        self.end = end 
        self.unemployment_path = unemployment_path
        self.income_path = income_path

    def edit_data(self):
        # editing the unemployment data
        print(self.start)
        self.income_data.rename(columns={ self.income_data.columns[-1]: 'hourly rate'}, 
                                inplace=True)
        self.income_data['year'] = self.income_data['DATE'].apply(lambda x: x[:4])
        self.income_data = self.income_data[self.income_data['year'] == self.start]
        self.income_data.set_index('DATE', inplace=True)
        self.income_data.pop('year')

        # editing the unemployment dataframe
        self.unemployment_data['year'] = self.unemployment_data['DATE'].apply(lambda x: x[:4])
        self.unemployment_data = self.unemployment_data[self.unemployment_data['year'] == self.start[:4]]
        self.unemployment_data.set_index('DATE', inplace=True)
        self.unemployment_data.pop('year')

    # getting the data for the 
    def get_data(self):
        self.unemployment_data = pd.read_csv(self.unemployment_path)
        self.income_data = pd.read_csv(self.income_path)
        # editing the data
        self.edit_data() 
        print(self.income_data.head())
        print(self.unemployment_data.head())

    # printing the data
    def print_data(self, xlabel, ylabel, title, fig_path):
        income_analysis = DataAnalyzer(self.income_path)
        income_analysis.plot_data(self.income_data, xlabel, ylabel, title, fig_path)

        unemployment_analysis = DataAnalyzer(self.unemployment_data)
        unemployment_analysis.plot_data(self.unemployment_data, xlabel, ylabel, title, fig_path)