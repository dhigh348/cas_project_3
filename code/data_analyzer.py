import matplotlib.pyplot as plt
import pandas as pd

class DataAnalyzer:

    # initializing the class
    def __init__(self, data):
        self.data = data 

    # function for normalizing the dataframe
    def normalize_dataframe(self) -> pd.DataFrame:
        data_norm = pd.DataFrame()
        for stock in self.data.columns:
            data_min = self.data[stock].min()
            data_max = self.data[stock].max()
            data_norm[stock] = (self.data[stock] - data_min) / (data_max - data_min)
        return data_norm

    # plotting generalized with passed data
    def plot_data(self, d, xlabel, ylabel, title, path) -> None:
        plt.figure(figsize=(14, 6))
        plt.plot(d)
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.title(title, fontsize=16)
        plt.legend(loc=(1.04,0))
        plt.savefig(path)