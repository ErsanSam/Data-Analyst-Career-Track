import pandas as pd
#buat dataframe df1 dan df2
df1 = pd.DataFrame({'a':[1,2],
                    'b':[3,4]})
df2 = pd.DataFrame({'b':[5,6],
                    'a':[7,8]})
row_wise_concat = pd.concat([df1,df2])
#TERAPKAN CONCAT ROW-WISE
print("ROW_WISE_CONCAT :\n", row_wise_concat)
#TERAPKAN CONCAT COLUMN-WISE
col_wise_concat = pd.concat([df1,df2], axis=1)
print("COLUMN_WISE_CONCAT:\n", col_wise_concat)
#PENAMBAHAN IDENTIFIER --> MEMBENTUK PENGGABUNGAN HASIL MULTIINDEX
multiindex_concat = pd.concat([df1,df2], axis=0,keys=['df1','df2'])
print("MULTIINDEX-CONCAT:\n",multiindex_concat)