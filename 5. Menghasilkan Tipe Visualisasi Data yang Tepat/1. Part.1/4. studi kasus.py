#[1]import library
import pandas as pd
import datetime
import matplotlib.pyplot as plt
#[2]baca dataset
dataset = pd.read_csv("retail_raw_reduced.csv")
#buat kolom order month
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime("%Y-%m"))
#buat kolom gmv
dataset['gmv'] = dataset['item_price']*dataset['quantity']
#plot grafik sessuai intruksi
plt.figure(figsize=(10,5))
dataset[dataset['order_month']=='2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(color='red',marker='.',linewidth=2)
plt.title("Daily Number of Customers - December 2019", loc='left',pad=30,fontsize=20,color='orange')
plt.xlabel('Order Date', fontsize=15, color='blue')
plt.ylabel('Number of Customers', fontsize=15, color='blue')
plt.grid(color='darkgray', linestyle=':',linewidth=0.5)
plt.ylim(ymin=0)
plt.show()