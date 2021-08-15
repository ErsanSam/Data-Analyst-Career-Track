#TRANSFORM
import pandas as pd
df = pd.read_csv("sample_csv.csv")
print("TIPE DATA DF: \n", df.dtypes)
df["order_date"] = pd.to_datetime(df["order_date"])
print("TIPE DATA SETELAH DI TRANSFORM:\n", df.dtypes)
print("___________________________________________________________")
#transform 2
import pandas as pd
df = pd.read_csv("sample_csv.csv")
print("TIPE DATA DF SEBELUM DI UBAH:\n", df.dtypes)
df["quantity"] = pd.to_numeric(df["quantity"], downcast="float")
df["city"] = df['city'].astype("category")
print("TIPE DATA DF SETELAH DI TRANSFORM: \n", df.dtypes)
#transform 3
import pandas as pd
df = pd.read_csv("sample_csv.csv")
print("KOLOM BRAND AWAL:\n", df["brand"].head())
#GUNAKAN METHOD .APLY untuk merubah isi kolom menjadi lower case <- UTK MENERAPKAN SUATU FUNGSI (DEF/LAMBDA) PADA DATAFRAME/SERIES ATAUHANYA KOLOM TERTENTU
df["brand"] = df["brand"].apply(lambda x: x.lower())
print("KOLOM BRAND SETELAH APPLY:\n", df["brand"].head())
#MENGGUNAKAN METHODE .map UNTUK MENGAMBILKARAKTER TERAKHIR KODE BRAND <- HANYA BISA SATU KOLOM YG DIAKSES
df["brand"] = df["brand"].map(lambda x:x[-1])
print("KOLOM BRAND SETELAH .map \n", df["brand"].head())
#TRANSFORMING 4 <- DATAFRAME
import pandas as pd
import numpy as np
#NUMBER GENERATOR, SET ANGKA SEET MENJADI SUATU ANGKA, BISA SEMUA ANGKA, SUPAYA HASIL RANDOMNYA SELALU SAMA KETIKA DI RUN
np.random.seed(1234)
#CREATE DATAFRAME 3 BARIS DAN 4 KOLOM DENGAN ANGKA RANDOM
df_tr = pd.DataFrame(np.random.rand(3,4))
print("DATAFRAME:::::\n",df_tr)
#CARA 1 DENGAN DEFINE FUNGSI AWALNYA, LANGSUNG PAKE FUNGSI ANONYMOUS LAMBDA X
df_tr1 = df_tr.applymap(lambda x: x**2 + 3*x +2)
print("\n DATAFRAME::::: CARA1\n", df_tr1)
#CARA2 DENGAN DEFINE FUNCTION
def quadratic_fun(x):
    return x**2 + 3*x + 2
df_tr2 = df_tr.applymap(quadratic_fun)
print("\n DATAFRAME::::: CARA2", df_tr2)