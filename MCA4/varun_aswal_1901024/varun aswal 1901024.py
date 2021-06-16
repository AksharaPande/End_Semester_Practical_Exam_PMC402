import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df_station_day = pd.read_csv('station_day.csv')

data

#data for stationid DL005 only
data=data.loc[data.StationID=='DL005'];
data

#describe the missing or null data in dataset
data.describe()

#as Xylene has no values so we wil remove it
ata=data.drop(['Xylene'],axis=1);

data['Benzene'].fillna(value=data['Benzene'].mean(), inplace=True)

data.dropna();

#histogram representation of PM10,NO,SO2 and O3 
data1=data[['PM10','NO','SO2','O3']]
data1.hist()



data.loc[:,['PM10','NO2','SO2','O3','AQI']].iloc[10:20,:]



#imputing AQI_Bucket column according to AQI column.
df_station_day.interpolate(method='linear',axis=0,limit_direction='both',inplace=True)
#imputing missing values using interpolation
def custom_imputer(df):
   if df['AQI'] < 51.0:
      return 'Good'
   elif 50.0<df['AQI']<101.0:
      return 'Satisfactory'
   elif 100.0<df['AQI']<201.0:
      return 'Moderate'
   elif 200.0<df['AQI']<301.0:
      return 'Poor'
   elif 300.0<df['AQI']<401.0:
      return 'Very Poor'
   else:
      return 'Severe'

df_station_day['AQI_Bucket'] = df_city_day.apply(custom_imputer,axis=1)