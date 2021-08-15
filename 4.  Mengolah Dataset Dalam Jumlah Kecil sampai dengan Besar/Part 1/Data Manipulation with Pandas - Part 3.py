#SLICING
import pandas as pd
df = pd.read_csv("sample_csv.csv")
#Slice langsung berdasarkan kolom
df_slice = df.loc[(df["order_date"]=='2019-01-01') &
                  (df['product_id'].isin(['P2154','P2556']))]
print("SLICE LANGSUNG BERDASARKAN KOLOM:\n", df_slice)
#slicing dengan .loc
#CARA1
import pandas as pd
df = pd.read_csv("sample_csv.csv")
df = df.set_index(['order_date','order_id','product_id'])
df_slice = df.loc[("2019-01-01",1612339,['P2154','P2159']),:]
print("SLICE DF 1:\n",df_slice)
#df_slice.to_excel("slice_df.xlsx", index = False)
#CARA1
import pandas as pd
df= pd.read_csv("sample_csv.csv")
df = df.set_index(['order_date','product_id'])
#gunakan .loc
df_slice1 = df.loc[('2019-01-01',['P2154','P2556']),:]
print("CARA 1 DF: \n", df_slice1)
#CARA2
idx = pd.IndexSlice
df_slice2 = df.sort_index().loc[idx["2019-01-01",'P2154':'P2556'],:]
print("CARA 2 DF:\n",df_slice2)