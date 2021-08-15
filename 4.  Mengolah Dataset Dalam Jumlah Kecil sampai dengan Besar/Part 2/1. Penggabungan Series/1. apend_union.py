import pandas as pd
#Buat series of int dan series of str
s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series(['a','b','c','d','e','f'])
#terapkan methode append
s2_append_s1 = s2.append(s1)
print("SERIES - APPEND:\n", s2_append_s1)
#buat dataframedf1 dan df2
df1 = pd.DataFrame({'a':[1,2],
                    'b':[3,4]})
df2 = pd.DataFrame({'b':[5,6],
                    'a':[7,8]})
#terapkan methode append
df1_append_df2 = df1.append(df2)
print("DATAFRAME - APPEND:\n", df1_append_df2)