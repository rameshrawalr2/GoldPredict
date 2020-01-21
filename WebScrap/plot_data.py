import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
from WebScrap.ARIMA import model
df = pd.read_csv("Gold_history_data.csv", parse_dates=['Date'])
# df = df.sort_values('Date',ascending=True)

df.Price_oz = df.Price_oz.apply(lambda x: x.replace(',',''))
df.Price_oz = df.Price_oz.apply(lambda x: int(x))
df.Price_g= df.Price_g.apply(lambda x: x.replace(',',''))
df.Price_g = df.Price_g.apply(lambda x: float(x))
# print(type(float(df['Price_g'].values[0])))
df= df[(df['Date']>datetime.datetime.strptime('2014-01-01','%Y-%m-%d'))&(df['Date']<datetime.datetime.strptime('2020-01-01','%Y-%m-%d'))]
df=df.reset_index()
price_lst = list(df.Price_g.values)
mean_lst = []
for index in range(len(price_lst)):
    mean_lst.append(np.mean(price_lst[index-5:index]))# + np.std(price_lst[index-5:index]))

# print(df.head(40))
# df = df[['Price_g']]
# df2 = df.Price_g[-20:]
# df =df.Price_g[:-20]
# df=df[:-10]
# print(df2.index)

# create a differenced series
def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - i]
        diff.append(value)
    return diff


# invert differenced forecast
def inverse_difference(last_ob, value):
    return value + last_ob


# define a dataset with a linear trend

# difference the dataset
# diff = difference(price_lst)
# print(diff)
# # invert the difference
# inverted = [inverse_difference(price_lst[i], diff[i]) for i in range(len(diff))]
# print(inverted)
# plt.plot(price_lst)
# plt.plot(diff)
# plt.show()
model = model(df)
# predict(df2)
plt.plot( df.Date.values, df.Price_g.values)
plt.plot( df.Date.values, mean_lst)
plt.scatter(df.Date.values, df.Price_g.values, marker='o',color='red', s=12)
plt.scatter(df.Date.values, mean_lst, marker='o',color='black', s=12)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
#
#
# import numpy as np, pandas as pd
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# import matplotlib.pyplot as plt
# import datetime
# plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})
#
# # Import data
# df = pd.read_csv("Gold_history_data.csv", parse_dates=['Date'])
# df= df[df['Date'] > datetime.datetime.strptime('2014-01-01','%Y-%m-%d')]
# df= df[df['Date'] < datetime.datetime.strptime('2014-11-01','%Y-%m-%d')]
# # df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/wwwusage.csv', names=['value'], header=0)
# df = df.rename(columns={'Price_g':'value'})
# df = df[['value']]
# df= df.reset_index()
# df.value = df.value.apply(lambda x: float(x.replace(',','')))
# print(type(df.value.tolist()[0]))
# # Original Series
# fig, axes = plt.subplots(4, 2, sharex=True)
# axes[0, 0].plot(df.value); axes[0, 0].set_title('Original Series')
# plot_pacf(df.value, ax=axes[0, 1])
#
# # 1st Differencing
# axes[1, 0].plot(df.value.diff()); axes[1, 0].set_title('1st Order Differencing')
# plot_pacf(df.value.diff().dropna(), ax=axes[1, 1])
#
# # 2nd Differencing
# axes[2, 0].plot(df.value.diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
# plot_pacf(df.value.diff().diff().dropna(), ax=axes[2, 1])
#
# # 3rd Differencing
# axes[3, 0].plot(df.value.diff().diff().diff()); axes[3, 0].set_title('3rd Order Differencing')
# plot_pacf(df.value.diff().diff().diff().dropna(), ax=axes[3, 1])
#
# plt.show()