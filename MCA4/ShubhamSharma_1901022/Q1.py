

from google.colab import files;
uploded=files.upload();

import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('station_day.csv');
data

data=data.loc[data.StationId=='DL005'];
data

data.describe()
print("Fraction of observations have missing values:\n",(data.isnull().sum())/len(data))

data= data[['PM10','NO','SO2','O3']]
data.hist()

"""PM2.5 has 722 values, PM10 has 692 values that means we have null values now. Xylene has 0 values that means it has only null in it so we have to remove that column"""

data=data.drop(['Xylene'],axis=1);

data['Benzene'].fillna(value=data['Benzene'].mean(), inplace=True)

data.dropna();

data1=data[['PM10','NO','SO2','O3']]
data1.hist()

data.loc[:,['PM10','NO2','SO2','O3','AQI']].iloc[10:20,:]
