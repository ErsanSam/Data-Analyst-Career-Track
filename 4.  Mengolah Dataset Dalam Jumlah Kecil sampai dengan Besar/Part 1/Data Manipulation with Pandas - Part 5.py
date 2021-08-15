#HANDLING MISSING VALUE
import pandas as pd
df = pd.read_csv("missing_value_covid.csv")
print(df.info)
mv = df.isna().sum() #gitung jumlah missing value disetiap kolom
print("\n JUMLAH MISSING VALUE PER KOLOM :\n", mv)
#MENGATASI MISSING VALUE =
#1 DIBIARKAN SAJA
#2 HAPUS VALUE ITU
#3 ISI VALUE TSB DENGAN VALUE YG LAIN(MEDIAN, MEAN, DLL)
##DROP / HAPUS KOLOM/BARIS
#CETAK UKURAN AWAL DATAFRAME
print("UKURAN AWAL DATAFRAME: %d baris, %d kolom." %df.shape)
#DROP KOLOM YG SELURUHNYA MISSING VALUE DAN CETAK UKURANNYA
df = df.dropna(axis=1, how="all")
print("UKURAN DF SETELAH BUANG KOLOM DENGAN SELURUH DATA MISSING:"
      "%d baris, %d kolom." %df.shape)
#DROP BARIS JIKA ADA SATU SAJA DATA YANG MISSING, LALU CETAK UKURANNYA
df = df.dropna(axis=0, how='any')
print("UKURAN DF SETELAH DIBANG BARIS YANG MEMILIKI SETIDAKNYA 1 MISSING VALUE:"
      "%d baris, %d kolom."%df.shape)
## MENGISI DENGAN string <- object=> string
import pandas as pd
df = pd.read_csv("missing_value_covid.csv")
print(df.info)
#cetak unique value pada kolom province_state
print("UNIQUE VALUE AWAL:\n",df['province_state'].unique())
#GANTI MISSING VALUE DENGAN STRING "unknown_province_state"
df['province_state'] = df['province_state'].fillna('unknown_province_state')
print("UNIQUE VALUE SETELAH FILLNA:\n", df['province_state'].unique())
#MENGISI DENGAN MEAN/MEDIAN
#MENGECEK DULU MEDIAN,MEAN,MIN,MAX. JIKA MEAN DAN MEDIAN HAMPIR SAMA, MAKA TERDISTRIBUSI NORMAL
#JIKA RANGE CUKUP LEBAR DAN PERBEDAAN MEDIA-MEAN YG CUKUP JAUH, TERDISTRIBUSI SKEWNESS
print("_________________________________")
import pandas as pd
df = pd.read_csv("missing_value_covid.csv")
print("AWAL:mean = %f, median = %f, max = %f, min= %f"
      %(df['active'].mean(),
        df['active'].median(),
        df['active'].max(),
        df['active'].min()))
#ISI MISSING VALUE KOLOM ACTIVE DENGAN MEDIAN
df_median=df['active'].fillna(df['active'].median())
print("FILLNA MEDIAN: mean = %f, median = %f"
      %(df_median.mean(), df_median.median()))
#ISI MISSING VALUE ACTIVE DENGAN MEAN
df_mean = df['active'].fillna(df['active'].mean())
print("FILLNA MEAN: mean = %f, median = %f"
      %(df_mean.mean(), df_mean.median()))
print("_______________________")
#INTERPOLASI LINEAR
import numpy as np
import pandas as pd
# Data
ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print(ts[1].mean())
print("Setelah diisi missing valuenya:\n", ts)
print(ts[1].mean())