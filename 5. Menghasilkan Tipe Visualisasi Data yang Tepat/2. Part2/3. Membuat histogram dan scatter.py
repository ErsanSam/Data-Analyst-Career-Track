# Import library
import datetime
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('retail_raw_reduced.csv') # Baca dataset
# Buat kolom baru yang bertipe datetime dalam format '%Y-%m'
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity'] # Buat Kolom GMV
dataset_dki_q4 = dataset[(dataset['province']=='DKI Jakarta')&(dataset['order_month']>='2019-10')] #membuat subset data
#Membuat Agregat Data Customer
data_per_customer = (dataset_dki_q4.groupby('customer_id')
                                   .agg({'order_id':'nunique',
                                         'quantity': 'sum',
                                         'gmv':'sum'})
                                   .reset_index()
                                   .rename(columns={'order_id':'orders'}))
print(data_per_customer.sort_values(by='orders',ascending=False))
#_____________________
import matplotlib.pyplot as plt
plt.clf()
# Histogram pertama
plt.figure()
plt.hist(data_per_customer['orders'])
plt.show()
# Histogram kedua
plt.figure()
plt.hist(data_per_customer['orders'],range=(1,5))
plt.title('Distribution of Number of Orders per Customer\nDKI Jakarta in Q4 2019',fontsize=15,color='blue')
plt.xlabel('Number of Orders',fontsize=12)
plt.ylabel('Number of Customers',fontsize=12)
plt.show()
#_________________________________
plt.figure(figsize=(10,5))
plt.hist(data_per_customer['quantity'],bins=100,range=(1,200),color='brown')
plt.title('Distribution of Total Quantity per Customer\nDKI Jakarta in Q4 2019',fontsize=15,color='blue')
plt.xlabel('Quantity',fontsize=12)
plt.ylabel('Number of Customers',fontsize=12)
plt.xlim(xmin=0,xmax=200)
plt.show()
#______________________________
plt.figure(figsize=(10,5))
plt.hist(data_per_customer['gmv'],bins=100,range=(1,200000000),color='green')
plt.title('Distribution of Total GMV per Customer\nDki Jakarta in Q4 2019',fontsize=15,color='blue')
plt.xlabel('GMV (in Millions)',fontsize=12)
plt.ylabel('Number of Customers',fontsize=12)
plt.xlim(xmin=0,xmax=200000000)
labels, locations = plt.xticks()
plt.xticks(labels, (labels/1000000).astype(int))
plt.show()
#_____________________________
plt.clf()
# Scatterplot pertama
plt.figure()
plt.scatter(data_per_customer['quantity'], data_per_customer['gmv'])
plt.show()
# Scatterplot kedua: perbaikan scatterplot pertama
plt.figure(figsize=(10,8))
plt.scatter(data_per_customer['quantity'],data_per_customer['gmv'],marker='+',color='red')
plt.title('Correlation of Quantity and GMV per Customer\nDKI Jakarta in Q4 2019',fontsize=15,color='blue')
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('GMV (in Millions)',fontsize=12)
plt.xlim(xmin=0,xmax=300)
plt.ylim(ymin=0,ymax=150000000)
labels, locations=plt.yticks()
plt.yticks(labels, (labels/1000000).astype(int))
plt.show()