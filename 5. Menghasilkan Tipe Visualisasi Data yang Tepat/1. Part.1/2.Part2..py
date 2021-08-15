#DATASET SETELAH DI AGGREGATE
import pandas as pd
monthly_amount = pd.read_csv('monthly_amount.csv')
print(monthly_amount)
#membuat chart dengan matplotlib
import matplotlib.pyplot as plt
plt.plot(monthly_amount['order_month'],monthly_amount['gmv'])
plt.show()
#membuat chart pada dataset
#import matplotlib.pyplot as plt
#dataset.groupby(['order_month'])['gmv'].sum().plot()
#plt.show()