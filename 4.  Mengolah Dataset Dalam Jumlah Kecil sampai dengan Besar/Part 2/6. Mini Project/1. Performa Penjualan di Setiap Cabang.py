#Goal: Automation untuk pembuatan grafik dari measurement yang dibutuhkan.
print('[1]. Load masing-masing data *.csv dengan Pandas')
import pandas as pd
import matplotlib.pyplot as plt
data_retail1 = pd.read_csv('retail_data1.csv', low_memory=False)
data_retail2 = pd.read_csv('retail_data2.csv', low_memory=False)
data_retail3 = pd.read_csv('retail_data3.csv', low_memory=False)
data_retail4 = pd.read_csv('retail_data4.csv', low_memory=False)
print("__________")
print("[2]. Pengecekan Data")
## Cek data sekilas (tampilkan 5 baris teratas)
print(data_retail1.head())
print(data_retail1.info())
# Cek list kolom untuk semua dataframe
print('Kolom retail_data1: %s' %data_retail1.columns)
print('Kolom retail_data2: %s' %data_retail2.columns)
print('Kolom retail_data3: %s' %data_retail3.columns)
print('Kolom retail_data4: %s' %data_retail4.columns)
# Concat multiple dataframe menjadi 1 dataframe
retail_table = pd.concat([data_retail1,data_retail2,data_retail3,data_retail4])
print('\nJumlah baris:', retail_table.shape[0])
# Pengecekan dataframe info
print('\nInfo:')
print(retail_table.info())
# Pengecekan statistik deskriptif
print('\nStatistik deskriptif:\n', retail_table.describe())
print('__________')
#[3] Transformasi Data
#1. Jika ada data yang tidak seharusnya maka dapat dibuang
#2. Jika ada kolom yang seharusnya bertipe datetime64 ubahlah
#3. Cek kembali informasi dataframe
#4. Tampilkan kembali statistik deskriptif dari dataframe
print('[3.] TRANSFORMASI DATA\n\n')
# Memastikan data yang memiliki item_price < 0 atau total_price < 0
cek = retail_table.loc[(retail_table['item_price'] < 0) | (retail_table['total_price'] < 0)]
print('\nitem_price < 0 atau total_price < 0:\n', cek)
# Jika tidak masuk akal datanya dapat dibuang
if cek.shape[0] != 0:
    retail_table = retail_table.loc[(retail_table['item_price'] > 0) & (retail_table['total_price'] > 0)]
# Cek apakah masih ada order_id yang bernilai undefined dan delete row tersebut
cek = retail_table.loc[retail_table['order_id'] == 'undefined']
print('\norder_id yang bernilai undefined:\n', cek)
# Jika ada maka buang baris tersebut
if cek.shape[0] != 0:
    retail_table = retail_table.loc[retail_table['order_id'] != 'undefined']
# Transform order_id menjadi int64
retail_table['order_id'] = retail_table['order_id'].astype('int64')
# Transform order_date menjadi datetime Pandas
retail_table['order_date'] = pd.to_datetime(retail_table['order_date'])
# Cek dataframe info kembali untuk memastikan
print('\nInfo:')
print(retail_table.info())
# Cek statistik deskriptif kembali, untuk memastikan
print('\nStatistik deskriptif:\n', retail_table.describe())
print("__________")
print("[4]. Filter province yang hanya termasuk 5 provinsi besar di Jawa (DKI Jakarta, Jawa Barat, Jawa Tengah, Jawa Timur, dan Yogyakarta)")
# [4]. Filter hanya 5 province terbesar di pulau Jawa
print('\nFILTER 5 PROVINCE TERBESAR DI PULAU JAWA\n')
java = ['DKI Jakarta','Jawa Barat','Jawa Tengah','Jawa Timur','Yogyakarta']
retail_table = retail_table.loc[retail_table['province'].isin(java)]
# Untuk memastikan kolom provinsi isinya sudah sama dengan java
print(retail_table['province'].unique())
print("__________")
#[5]. Mengelompokkan data berdasarkan order_date dan province yang sudah difilter
# dan menghitung order unique count, customer unique count, product unique count, brand unique count,
# dan GMV (Gross Merchandise Volume = total_price untuk semua penjualan)
print("[5]. Kelompokkan sesuai dengan order_date dan province kemudian aggregasikan")
groupby_city_province = retail_table.groupby(['order_date','province']).agg({
	'order_id': 'nunique',
	'customer_id': 'nunique',
	'product_id': 'nunique',
	'brand': 'nunique',
	'total_price': sum
})
# Ubah nama kolomnya menjadi 'order','customer','product','brand','GMV'
groupby_city_province.columns = ['order','customer','product','brand','GMV']
print('\ngroupby_city_province (10 data teratas):\n', groupby_city_province.head(10))
print("__________")
print('[6]. Unstack untuk mendapatkan order_date di bagian baris dan province di bagian column')
unstack_city_province = groupby_city_province.unstack('province').fillna(0)
print('\nunstack_city_province (5 data teratas):\n', unstack_city_province.head())
print("__________")
print('[7]. Slicing data untuk masing-masing measurement, misal: order')
idx = pd.IndexSlice
by_order = unstack_city_province.loc[:,idx['order']]
print('\nby order (5 data teratas):\n', by_order.head())
print('[8]. Lakukan resampling pada data tersebut untuk dilakukan perhitungan rata-rata bulanan')
by_order_monthly_mean = by_order.resample('M').mean()
print('\nby_order_monthly_mean (5 data teratas):\n', by_order_monthly_mean.head())
print("__________")
print(" [9]. Plot untuk hasil pada langkah #[8]")
by_order_monthly_mean.plot(figsize = (8,5),
						   title = 'Average Daily order Size in Month View for all Province')
plt.ylabel('avg order size')
plt.xlabel('month')
plt.show()
print("Dapat dilihat bahwa avg order size untuk DKI Jakarta tertinggi dan terus memiliki kenaikan,"
	  " disusul oleh Jawa Barat dan kemudian 3 sisanya hampir berada dalam angka yang rata-rata sama")
print("Langah 7 s/d 9 yang telah dilakukan baru untuk satu measurement yaitu order. "
	  "Berarti ada empat kali lagi kode seperti ini harus dibuat. "
	  "Karena struktur code masih sama, dapat menggunakan perulangan sesuai dengan jumlah measurement yaitu 5,"
	  " sehingga kelima measurement dapat ditampilkan grafiknya dalam satu canvas figure.")

print("Mari memulai dengan membuat sebuah perulangan dengan dataframe unstack_city_province yang digunakan (hasil dari langkah ke 5 di part 2).")
# Create figure canvas dan axes for 5 line plots
fig, axes = plt.subplots(5, 1, figsize=(8, 25))

# Slicing index
idx = pd.IndexSlice
for i, measurement in enumerate(groupby_city_province.columns):
# Slicing data untuk masing-masing measurement
	by_measurement = unstack_city_province.loc[:,idx[measurement]]
# Lakukan resampling pada data tersebut untuk dilakukan perhitungan rata-rata bulanan
	by_measurement_monthly_mean = by_measurement.resample('M').mean()
# Plot by_measurement_monthly_mean
	by_measurement_monthly_mean.plot(title = 'Average Daily ' + measurement + ' Size in Month View for all Province',
									 ax = axes[i])
	axes[i].set_ylabel('avg ' + measurement + ' size')
	axes[i].set_xlabel('month')

# Adjust the layout and show the plot
plt.tight_layout()
plt.show()