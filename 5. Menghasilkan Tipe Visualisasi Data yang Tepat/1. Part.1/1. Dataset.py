import pandas as pd
dataset = pd.read_csv('retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' %dataset.shape)
print('Lima data teratas:')
print(dataset.head())
print("__________")
print('Penambahan Kolom Order Month pada Dataset\n')
import datetime
dataset['order_month']=dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())
print("Penambahan Kolom GMV pada Dataset\n")
dataset['gmv']=dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())
print("__________")
print('[2] PLOT PERTAMA MENGGUNAKAN MATPLOTLIB')
#dataset.to_csv('dataset.csv')
#Membuat Data Agregat
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)
#monthly_amount.to_csv('monthly_amount.csv')