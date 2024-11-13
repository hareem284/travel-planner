#importing matplotlib 
import matplotlib.pyplot as plt
#importing pandas
import pandas as pd
#reading csv file
df=pd.read_csv("Weather.csv")
print(df.head())
print(df.tail())
dfgroup=df.groupby('month').mean()
dfgroup=dfgroup.reset_index()
print(dfgroup.head())
dfgroup.plot.area(x='month',y='Humidity')
#plt.show()
plt.plot(df['Temperature (C)'])
plt.xlabel("READING")
plt.ylabel("TEMPERATURE")
plt.show()