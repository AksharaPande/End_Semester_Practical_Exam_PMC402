
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv('station_day.csv')
df.head()

df = pd.read_csv('station_day.csv');


df=df.loc[data.StationId=='DL005'];


df.describe()

"""PM2.5 has 722 values whereas PM10 has 692 values that means we have null values in our data ... xylene has 0 values that means it has only null in it so we will remove that column"""

df=df.drop(['Xylene'],axis=1);

df['Benzene'].fillna(value=df['Benzene'].mean(), inplace=True)

df.dropna();

df1=df[['PM10','NO','SO2','O3']]
df1.hist()

df.loc[:,['PM10','NO2','SO2','O3','AQI']].iloc[10:20,:]