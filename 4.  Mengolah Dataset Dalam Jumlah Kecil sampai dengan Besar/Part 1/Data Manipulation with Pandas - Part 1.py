#IMPORT PANDAS DAN NUMPY
import pandas as pd
import numpy as np
#Series
number_list = pd.Series([1,2,3,4,5,6])
print("Series :")
print(number_list)
#Dataframe
matrix = [[1,2,3],
          ['a','b','c'],
          [3,4,5],
          ['d',4,6]]
matrix_list = pd.DataFrame(matrix)
print("DataFrame :")
print(matrix_list)
#atribut series dan dataframe
# [1] attribute .info(), mengecek kolom apa yg membentuk dataframe
print("[1] attribute .info()")
print(matrix_list.info())
# [2] attribute .shape, mengetahui jumlah baris dan kolom
print("\n[2] attribute .shape")
print("    Shape dari number_list:", number_list.shape)
print("    Shape dari matrix_list:", matrix_list.shape)
# [3] attribute .dtypes, mengetahui tipe data di tiap kolom.
# Tipe data object: kombinasi untuk berbagai tipe data (number & text, etc).
print("\n[3] attribute .dtypes")
print("    Tipe data number_list:", number_list.dtypes)
print("    Tipe data matrix_list:", matrix_list.dtypes)
# [4] attribute .astype(),
# Attribute .astype(nama_tipe_data) untuk convert tipe data berdasarkan tipe data
# seperti: float, int, str, numpy.float, numpy.int ataupun numpy.datetime.
print("\n[4] attribute .astype()")
print("    Konversi number_list ke str:", number_list.astype("str"))
print("    Konversi matrix_list ke str:", matrix_list.astype("str"))
# [5] attribute .copy(), Attribute .copy() digunakan melakukan duplikat,
# untuk disimpan di variable yang berbeda mungkin supaya tidak loading data lagi.
print("[5] attribute .copy()")
num_list = number_list.copy()
print("    Copy number_list ke num_list:", num_list)
mtr_list = matrix_list.copy()
print("    Copy matrix_list ke mtr_list:", mtr_list)
# [6] attribute .to_list(),
# Attribute .to_list()
# digunakan untuk mengubah series menjadi list dan tidak dapat digunakan untuk dataframe.
print("[6] attribute .to_list()")
print(number_list.to_list())
# [7] attribute .unique()
#Attribute .unique() digunakan menghasilkan nilai unik dari suatu kolom,
# hasilnya dalam bentuk numpy array. Attribute ini hanya digunakan pada series saja.
print("[7] attribute .unique()")
print(number_list.unique())
# [8] attribute .index
#Attribute .index digunakan untuk mencari index/key dari Series atau Dataframe.
print("[8] attribute .index")
print("    Index number_list:", number_list.index)
print("    Index matrix_list:", matrix_list.index)
# [9] attribute .columns
#Digunakan untuk mengetahui apa saja kolom yang tersedia di dataframe tersebut
# (hanya digunakan untuk dataframe saja).
print("[9] attribute .columns")
print("    Column matrix_list:", matrix_list.columns)
# [10] attribute .loc
#digunakan slice dataframe atau series berdasarkan nama kolom dan/atau nama index.
print("[10] attribute .loc")
print("    .loc[0:1] pada number_list:", number_list.loc[0:1])
print("    .loc[0:1] pada matrix_list:", matrix_list.loc[0:1])
# [11] attribute .iloc
#digunakan untuk slice dataframe atau series berdasarkan index kolom dan/atau index.
print("[11] attribute .iloc")
print("    iloc[0:1] pada number_list:", number_list.iloc[0:1])
print("    iloc[0:1] pada matrix_list:", matrix_list.iloc[0:1])
#Creating Series & Dataframe from List
# Creating series from list
ex_list = ['a',1,3,5,'c','d']
ex_series = pd.Series(ex_list)
print("ex series")
print(ex_series)
# Creating dataframe from list of list
ex_list_of_list = [[1,'a','b','c'],
                   [2.5,'d','e','f'],
		           [5,'g','h','i'],
		           [7.5,'j',10.5,'l']]
index = ['dq','lab','kar','lan']
cols = ['float','char','obj','char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)
#Creating Series & Dataframe from Dictionary
# Creating series from dictionary
dict_series = {'1':'a',
			   '2':'b',
			   '3':'c'}
ex_series = pd.Series(dict_series)
print("ex_series")
print(ex_series)
# Creating dataframe from dictionary
df_series = {'1':['a','b','c'],
             '2':['b','c','d'],
             '4':[2,3,'z']}
ex_df = pd.DataFrame(df_series)
print("ex_df")
print(ex_df)
#Creating Series & Dataframe from Numpy Array
# Creating series from numpy array (1D)
arr_series = np.array([1,2,3,4,5,6,6,7])
ex_series = pd.Series(arr_series)
print("ex_series")
print(ex_series)
# Creating dataframe from numpy array (2D)
arr_df = np.array([[1,2,3,5],
                   [5,6,7,8],
                   ['a','b','c',10]])
ex_df = pd.DataFrame(arr_df)
print("ex_df")
print(ex_df)
#Read Dataset -
# File CSV
df_csv = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx",
                         sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas
# File JSON
url = "https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas
'''
#Read Dataset - MYSQL
import mysql.connector
#membuat konenksi ke databease financial di https://relational.fit.cvut.cz/datasaet/Financial
my_conn = mysql.connector.connect(
    host = "relational.fiz.cvut.cz",
    port = 3306,
    user = "guest",
    passwd = "relational",
    database = "financial",
    use_pure = True
)
#buat query sql utk tabel loan
my_querry = ''
SELECT * FROM loan;''
#gunakan .read_sql_query utk membaca tabel load tsb
df_loan = pd.read_sql_query(my_querry, my_conn)
df_loan.head(10)
'''
