print("[1] DATA PREPARATION")
import pandas as pd
dataset = pd.read_csv("data_retail.csv", sep=';')
#tampilkan 5 data teratas dan info dataset
print('Lima Data Teratas:\n', dataset.head())
#tampilkan info dataset
print("Informasi Dataset:\n", dataset.info())
print("__________")
print("[2] DATA CLEANSING")
#mengubah 2 kolom yg berisi informasi terjadinya transaksi dari tipe object ke tipe datetime
#kolom First Transaction
dataset['First_Transaction'] = pd.to_datetime(dataset['First_Transaction']/1000, unit='s', origin = '1970-01-01')
#kolom Last Transaction
dataset['Last_Transaction'] = pd.to_datetime(dataset['Last_Transaction']/1000, unit='s', origin='1970-01-01')
#cek ulang dataset
print("Lima Data teratas:\n", dataset.head())
print("Informasi Dataset:\n", dataset.info())
print("__________")
print("[2a] Klasifikasi pelanggan yg bertipe churn") # churn= customer yg melakukan pembelian 6 bulan terakhir
#Pengecekan transaksi terakhir pelanggan
print(max(dataset['Last_Transaction'])) # <- 2019-02-01
#Klasifikasi pelanggan yg bertipe churn atau tidak
dataset.loc[dataset['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True
dataset.loc[dataset['Last_Transaction'] > '2018-08-01', 'is_churn'] = False
#cek ulang dataset
print("Lima Data Teratas:\n", dataset.head())
print('Informasi Dataset:\n', dataset.info())
print("__________")
print("[2b] Menghapus kolom-kolom yg tidak diperlukan")
del dataset['no']
del dataset['Row_Num']
print(dataset.head())
print(dataset.info())
print("__________")
print('[3] Vizualisation')
print("[3a] Customer acquisition by year")
import matplotlib.pyplot as plt

# Kolom tahun transaksi pertama
dataset['Year_First_Transaction'] = dataset['First_Transaction'].dt.year
# Kolom tahun transaksi terakhir
dataset['Year_Last_Transaction'] = dataset['Last_Transaction'].dt.year

df_year = dataset.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()
print("[3b] Transaksi per tahun")
plt.clf()
df_year = dataset.groupby(['Year_First_Transaction'])['Count_Transaction'].sum()
df_year.plot(x='Year_First_Transaction', y='Count_Transaction', kind='bar', title='Graph of Transaction Customer')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Transaction')
plt.tight_layout()
plt.show()
print("[3c] Average Transaction Amount by Year")
import seaborn as sns
plt.clf()
sns.pointplot(data = dataset.groupby(['Product', 'Year_First_Transaction']).mean().reset_index(),
x='Year_First_Transaction',
y='Average_Transaction_Amount',
hue='Product')
plt.tight_layout()
plt.show()
print("[3d] Proporsi churned customer untuk setiap produk")
plt.clf()
# Melakukan pivot data
dataset_piv = dataset.pivot_table(index='is_churn',
                                  columns='Product',
                                  values='Customer_ID',
                                  aggfunc='count',
                                  fill_value=0)
# Mendapatkan Proportion Churn by Product
plot_product = dataset_piv.count().sort_values(ascending=False).head(5).index
# Plot pie chartnya
df_piv = dataset_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product')
plt.tight_layout()
plt.show()