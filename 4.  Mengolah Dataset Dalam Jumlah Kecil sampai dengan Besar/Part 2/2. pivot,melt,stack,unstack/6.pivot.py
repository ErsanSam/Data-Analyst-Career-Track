##DATAFRAME
import pandas as pd
data = pd.DataFrame({
    'kelas':6*['A'] + 6*['B'],
    'murid': 2*['A1'] + 2*['A2'] + 2*['A3'] + 2*['B1'] + 2*['B2'] + 2*['B3'],
    'pelajaran': 6*['math','english'],
    'nilai':[90,60,70,85,50,60,100,40,95,80,60,45]
},columns=['kelas','murid','pelajaran','nilai'])
#UNIQUE VALUE PADA SETIAP KOLOM DATA
for column in data.columns:
    print('Unique value %s: %s' %(column,data[column].unique()))
print(data.info())
print("_________________________________")
#PIVOT
#pivoting with single column measurement
pivot1 = data.pivot(index='murid',columns='pelajaran',values='nilai')
print("PIVOTING WITH SINGLE COLUMN MEASUREMENT:\n", pivot1)
print(pivot1.info())
pivot2 = data.pivot(index='murid',columns='pelajaran')
print("PIVOTING WITH MULTIPLE COLUMN MEASUREMENT:\n", pivot2)
print(pivot2.info())
#CREATING PIVOT AND ASSIGN PIVOT_TAB DENGAN MENGGUNAKAN KEYWORD AGGFUNC=MEDIAN
pivot_tab_mean=data.pivot_table(index='kelas',
                                columns='pelajaran',
                                values='nilai',
                                aggfunc='mean')
print("Creating Pivot Table -- aggfunc=mean:\n", pivot_tab_mean)
print(pivot_tab_mean.info())
#CREATING PIVOT AND ASSIGN PIVOT_TAB DENGAN MENGGUNAKAN KEYWORD AGGFUNC=MEDIAN
pivot_tab_median=data.pivot_table(index='kelas',
                                columns='pelajaran',
                                values='nilai',
                                aggfunc='median')
print("Creating Pivot Table -- aggfunc=median:\n", pivot_tab_median)
print(pivot_tab_median.info())