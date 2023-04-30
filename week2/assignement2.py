#matpotlib tutorial
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pprint

#falta quitar 2015
df=pd.read_csv("data.csv")
df.sort_values(by=['Date'], inplace=True)
# df['Date']=pd.to_datetime(df['Date'], format="%Y-%m-%d")
df['Date']=pd.to_datetime(df.Date)
# print(df)

mask=(df['Date']>='2015-01-01')
df_2015=df.where(mask).dropna()
df_2015.sort_values(by=['ID', 'Date'], inplace=True)
df_2015_max= df_2015.groupby([(df.Date.dt.month),(df.Date.dt.day)])['Data_Value'].max()
df_2015_min= df_2015.groupby([(df.Date.dt.month),(df.Date.dt.day)])['Data_Value'].min()

datosmax_2015=[]
for x in df_2015_max:
    datosmax_2015.append(x/10)
# print(datosmax_2015)
# print(len(datosmax_2015))
# print('\n')

datosmin_2015=[]
for y in df_2015_max:
    datosmin_2015.append(y/10)
# print(datosmin_2015)
# print(len(datosmin_2015))
#------------------------------------------------------------"
mask1=(df['Date']<'2015-01-01')
df2005_14=df.where(mask1).dropna()
df2005_14.sort_values(by=['ID', 'Date'], inplace=True)
df2005_14_max= df2005_14.groupby([(df.Date.dt.month),(df.Date.dt.day)])['Data_Value'].max()
df2005_14_min= df2005_14.groupby([(df.Date.dt.month),(df.Date.dt.day)])['Data_Value'].min()
# print(df2005_14)

datosmax2005_14=[]
for d in df2005_14_max:
    datosmax2005_14.append(d/10)
datosmax2005_14.pop(59)        #elimino el valor correpondiente a la fecha 29-feb = valor #60
# print(datosmax2005_14)
# print(len(datosmax2005_14))
# print('\n')

datosmin2005_14=[]
for f in df2005_14_min:
    datosmin2005_14.append(f/10)
datosmin2005_14.pop(59)       #elimino el valor correpondiente a la fecha 29-feb = valor #60
# print(datosmin2005_14)
# print(len(datosmin2005_14))
# print('\n')

b=range(365)
scatter_max=list(b) #quedaran las posiciones donde el valor de 2015 supera el del periodo 2005-2014
cont=0
xx=[]
yy=[]
for n in range(365):
    if datosmax_2015[n] > datosmax2005_14[n]:
        scatter_max[n]=datosmax_2015[n]
        xx.append(cont)
        yy.append(datosmax_2015[cont])
    else:
        scatter_max[n]=0
    cont=cont+1
# print(xx)
# print(len(xx))
# print(yy)
# print(len(yy))


x_ticks_labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
x_values=[30,60,90,120,150,180,210,240,270,300,330,360]

plt.figure()
plt.scatter(xx,yy,s=5, c='green')
# plot the linear data and the exponential data
plt.plot(datosmax2005_14,'-r',datosmin2005_14, '-b')
# plt.xlabel('Days of year')
plt.ylabel('Temperature (°c)')
plt.title(' Ann Arbor, Michigan, United States 2005-14 Registers')
plt.legend(['Temp.Max','Temp.Min','Day-Broke record.2015'], frameon=False)
plt.gca().fill_between(range(len(datosmax2005_14)),datosmax2005_14, datosmin2005_14, facecolor='black', alpha=0.3)
# x = plt.gca().xaxis
# for item in x.get_ticklabels():
#     item.set_rotation(45)
# plt.subplots_adjust(bottom=0.25)
ax=plt.gca()
ax.get_xaxis().set_ticks(x_values)
ax.set_xticklabels(x_ticks_labels)

# ax.set_xlabel('Months of year')

###### Use the below functions #######
# dtFmt = mdates.DateFormatter('%b') # define the formatting
# plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
plt.show()
