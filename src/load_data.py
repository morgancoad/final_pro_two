# from sklearn.model_selection import train_test_split, KFold
# from sklearn.pipeline import Pipeline
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# import numpy as np
import pandas as pd
# import statistics
# import seaborn as sns
# import matplotlib.pyplot as plt



# plt.style.use('ggplot')

def load_data(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe

load_data('../data/crimes_by_county.csv')



if __name__ == '__main__':
#     dataframe = 
    load_data('../data/crimes_by_county.csv')
    print('test')
    