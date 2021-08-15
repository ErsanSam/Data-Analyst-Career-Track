import pandas as pd
df1 = pd.DataFrame({
    'key':['k1','k2','k3','k4','k5'],
    'val1':[200,500,0,500,100],
    'val2':[30,50,100,20,10]
})
df2 = pd.DataFrame({
    'key':['k1','k3','k5','k7','k10'],
    'val3':[1,2,3,4,5],
    'val4':[6,7,8,8,10]
})
#MERGE YG EKUIVALEN DENGAN SQL LEFT JOIN
merge_df_left = pd.merge(left=df1,
                         right=df2,
                         how='left',
                         left_on='key',
                         right_on='key')
print("MERGE - LEFT:\n",merge_df_left)
#MERGE YG EKUIVALEN DENGAN SQL RIGHT JOIN
merge_df_right = pd.merge(left=df1,
                          right=df2,
                          how='right',
                          left_on='key',
                          right_on='key')
print("MERGE - RIGHT:\n", merge_df_right)
#MERGE YG EKUIVALEN DENGAN SQL INNER JOIN
merge_df_inner = pd.merge(left=df1,
                          right=df2,
                          how='inner',
                          left_on='key',
                          right_on='key')
print("MERGE - INNER:\n", merge_df_inner)
#MERGE YG EKUIVALEN DENGAN SQL OUTER JOIN
merge_df_outer = pd.merge(left=df1,
                          right=df2,
                          how='outer',
                          left_on='key',
                          right_on='key')
print("MERGE - OUTER:\n", merge_df_outer)
##Part2
import pandas as pd
df1 = pd.DataFrame({
    'key':['k1','k2','k3','k4','k5'],
    'val1':[200,500,0,500,100],
    'val2':[30,50,100,20,10]
}).set_index(['key','val2'])
print("DATAFRAME-1:\n", df1)
df2 = pd.DataFrame({
    'key':['k1','k3','k5','k7','k10'],
    'val3':[1,2,3,4,5],
    'val4':[6,7,8,8,10]
}).set_index(['key','val3'])
print("DATAFRAME-2:\n", df2)
#MERGE DATAFRAME YG MEMILIKI MULTI INDEX
df_merge = pd.merge(df1.reset_index(),df2.reset_index())
print("MERGING DATAFRAME:\n",df_merge)
