#melt = mengembalikan data yg telah di pivot menjadi sebelumnya
##DATAFRAME
import pandas as pd
data = pd.DataFrame({
    'kelas':6*['A'] + 6*['B'],
    'murid': 2*['A1'] + 2*['A2'] + 2*['A3'] + 2*['B1'] + 2*['B2'] + 2*['B3'],
    'pelajaran': 6*['math','english'],
    'nilai':[90,60,70,85,50,60,100,40,95,80,60,45]
},columns=['kelas','murid','pelajaran','nilai'])
print("_________________________________")
#PIVOT
pivot_tab_mean=data.pivot_table(index='kelas',
                                columns='pelajaran',
                                values='nilai',
                                aggfunc='mean').reset_index()
print("Creating Pivot Table -- aggfunc=mean:\n", pivot_tab_mean)
print(pivot_tab_mean.info())
#melting dataframe
data_melt1=pd.melt(pivot_tab_mean)
print("Melting dataframe:\n",data_melt1)
#melting dataframe dengan id_vars
data_melt2 = pd.melt(pivot_tab_mean, id_vars='kelas')
print("Melting dataframe dengan id_vars:\n",data_melt2)
print("_________________________")
# Pivoting dataframe
data_pivot = data.pivot_table(index='kelas',columns='pelajaran',values='nilai', aggfunc='mean').reset_index()
print('Pivoting dataframe:\n', data_pivot)
# [3.a] Melting dataframe data_pivot dengan value_vars
data_melt_3a = pd.melt(data_pivot,value_vars=['math'])
print('Melting dataframe dengan value_vars:\n', data_melt_3a)
# [3.b] Melting dataframe data_pivot dengan id_vars dan value_vars
data_melt_3b = pd.melt(data_pivot, id_vars='kelas', value_vars=['math'])
print('Melting dataframe dengan id_vars dan value_vars:\n', data_melt_3b)
# [4] Melting dataframe data_pivot dengan id_vars, value_vars, var_name. dan value_name
data_melt_4 = pd.melt(data_pivot, id_vars='kelas',value_vars=['english','math'],var_name='pelajaran',value_name='nilai')
print('Melting dataframe dengan id_vars, value_vars, var_name. dan value_name:\n', data_melt_4)