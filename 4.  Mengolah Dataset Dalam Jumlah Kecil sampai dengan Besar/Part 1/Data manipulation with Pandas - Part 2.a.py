#head and Tail
import pandas as pd
#baca file sample_csv
df = pd.read_csv("sample_csv.csv")
#tampilkan 3 baris teratas
print("Tiga data teratas:\n", df.head(3))
#tampilkan 3 baris terbawah
print("Tiga data terbawah:\n", df.tail(3))
#INDEXING, SLICING, TRANSFORMING
#INDEXING
import pandas as pd
#baca file sample_tsv.tsv
df = pd.read_csv("sample_tsv.tsv", sep="\t")
#INDEX DARI DF
print("Index dari DF:\n",df.index)
#COLUMN DARI INDEX DF
print("COLUMN DARI DF:\n",df.columns)
#MULTI INDEX/ HIERARCHIAL INDEX
print("MULTI INDEX DF:")
import pandas as pd
df = pd.read_csv("sample_tsv.tsv", sep="\t")
#set multi index df
df_x = df.set_index(['order_date','city','customer_id'])
#print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,":",level)
#INDEXING 4
import pandas as pd
df = pd.read_csv("sample_tsv.tsv", sep ="\t", nrows=10)
#cetak data frame awal
print("DATAFRAME AWAL:\n",df)
#SET INDEX BARU
df.index = ["Pesanan ke-"+ str(i) for i in range(1,11)] #CETAK DATAFRAME DENGAN INDEX BARU
print("DATAFRAME DENGAN INDEX BARU:\n",df)
