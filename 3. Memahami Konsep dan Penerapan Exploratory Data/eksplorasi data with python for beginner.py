#mengimport library
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#Membaca file dari Excel atau CSV sebagai data frame
order_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/order.csv')
#Inspeksi struktur data frame. Melihat struktur kolom dan baris dari data frame
print("order df.shape :", order_df.shape)
#Melihat preview data dari data frame
print("order_df.head(10):", order_df.head(10))
#Statistika
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print("order_df.describe :",order_df.describe(include = 'all'))
print("info",order_df.info())
print("columns",order_df.columns)
print("count",order_df.count())
# Median median dari total pembelian konsumen per transaksi kolom price
print("order_df.loc[:, price].median() :" ,order_df.loc[:, "price"].median())
#Mengenal dan Membuat Distribusi Data dengan Histogram
#plot histogram kolom price
order_df[['price']].hist(figsize=(4, 5),
                         bins=10,
                         xlabelsize=8,
                         ylabelsize =8,
                         alpha= 1)
#plt.show()
#Standar Deviasi dan Varians pada Pandas
# Standar variasi kolom product_weight_gram
print("order_df.loc[:, 'product_weight_gram'].std():",order_df.loc[:, "product_weight_gram"].std())
# Varians kolom product_weight_gram
print("order_df.loc[:, 'product_weight_gram'].var():" ,order_df.loc[:, "product_weight_gram"].var())
#Menemukan Outliers Menggunakan Pandas
#dikatakan outliers jika memenuhi.
# data < Q1 - 1.5 * IQR
#data > Q3 + 1.5 * IQR
# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3-Q1
print("NILAI IQR:",IQR)
print("IDENTIFIKASI OUTLEAR:")
print((order_df < (Q1-1.5*IQR))| (order_df > (Q3 + 1.5*IQR)))
#Rename Kolom Data Frame
#1. Rename menggunakan nama kolom
#2. Rename menggunakan indeks kolom
# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
order_df.columns.values[3] = "harga"
print(order_df.columns)
#.groupby menggunakan Pandas
# Hitung rata rata dari price per payment_type
rata_rata = order_df["harga"].groupby(order_df["payment_type"]).mean()
print(rata_rata)
#Sorting Menggunakan Pandas
# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="harga", ascending=0)
print(sort_harga)
#Tugas dari Andra
# Untuk product_category_name, berapa rata-rata weight produk tersebut
# dan standar deviasi mana yang terkecil dari weight tersebut,
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print("MEAN_VALUE",mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print("STD",std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()