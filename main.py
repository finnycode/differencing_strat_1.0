import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import time as t
import random


df = pd.read_csv('AAPL_data.csv')




#make all date values of df the datetime
df['date'] = pd.to_datetime(df['date'])

#create a difference model for the close prices in df
df['Close_diff'] = df['close'].diff()


#make df only have the date and close_diff and close columns
df = df[['date', 'Close_diff', 'close']]

    
#make df a pandas dataframe with only 100 rows
#df = df.head(100)





profitl = []
profit = 0
short_trades = 0
long_trades = 0
win_rate = 0
#for every price in close_diff, if it is above or below its mean + 2*std, then print it and its date and next df['close'] value + profit and such
for i in range(len(df) - 2):
    if df['Close_diff'][i] > df['Close_diff'].mean() + 2*df['Close_diff'].std():
        print("Above")
        print(df['date'][i], df['Close_diff'][i])
        print("First close price: ", df['close'][i])
        print("Next Close Price: ", df['close'][i+2])
        print("Profit: " + str(df['close'][i] - df['close'][i+2]))
        profit += (df['close'][i] - df['close'][i+2])
        profitl.append(df['close'][i] - df['close'][i+2])
        short_trades += 1
        if profitl[-1] > 0:
            win_rate += 1
    elif df['Close_diff'][i] < df['Close_diff'].mean() - 2*df['Close_diff'].std():
        print("Below")
        print(df['date'][i], df['Close_diff'][i])
        print("First close price: ", df['close'][i])
        print("Next Close Price: ", df['close'][i+2])
        print("Profit: " + str(df['close'][i+2] - df['close'][i]))
        profit += (df['close'][i+2] - df['close'][i])
        profitl.append(df['close'][i+2] - df['close'][i])
        long_trades += 1
        if profitl[-1] > 0:
            win_rate += 1
    else:
        print("Nothing")
        
print('\n' + "Total profit: " + str(sum(profitl)))
print("Max profit: " + str(max(profitl)))
print("Min profit: " + str(min(profitl)))
print("Short trades: " + str(short_trades))
print("Long trades: " + str(long_trades))
print("Win rate: %" + str(win_rate/len(profitl)))
#plot close_diff and the df[date] values
plt.plot(df['date'], df['Close_diff'])


plt.plot(df['date'], (df['close']/100)**(-1/2), color = 'black')

#plot the close_diff mean
plt.axhline(df['Close_diff'].mean(), color='red')
#plot the close_diff 2 population standard deviation + and - mean
plt.axhline(df['Close_diff'].mean() + 2*df['Close_diff'].std(), color='green')
plt.axhline(df['Close_diff'].mean() - 2*df['Close_diff'].std(), color='green')

plt.show()

