import pandas as pd
matrix = [[0,1,2],
          [3,4,5],
          [6,7,8],
          [9,10,11]]
matrix_list = pd.DataFrame(matrix)
print(matrix_list.iloc[0:3,2].to_list())