import pandas as pd
# from . import html5lib
from bs4 import BeautifulSoup
# import html5lib
from datetime import  datetime
import urllib3
http = urllib3.PoolManager()
final_df = pd.DataFrame()
for year in range(11,20):
    for month in  range(1,13):
        # print(year, month)
        url = 'https://www.bullion-rates.com/gold/NPR/20'+str(year)+'-'+str(month)+'-history.htm'
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data,'lxml')

        hsgrid = soup.find('td','HistoryGrid')

        data_rows = hsgrid.find_all('tr','DataRow')
        date = []
        price_oz = []
        price_g = []
        for data in data_rows:
            rate = data.find_all('td')
            data= []
            for r in rate:
                data.append(r.text)

            date.append(datetime.strptime(data[0],"%x"))
            # print(date.date())
            price_oz.append(data[1])
            price_g.append(data[2])
        df = pd.DataFrame({"Date":date, 'Price_oz':price_oz, 'Price_g':price_g})
        # print(df)
        final_df = final_df.append(df)
print(final_df)
final_df.to_csv("Gold_history_data.csv",index=False)

