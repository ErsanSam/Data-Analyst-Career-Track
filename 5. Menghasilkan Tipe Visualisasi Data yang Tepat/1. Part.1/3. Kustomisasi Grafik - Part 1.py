import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("dataset.csv")
print(dataset.head())
plt.figure(figsize=(15,5)) #Mengubah Figure Size
dataset.groupby(['order_month'])['gmv'].sum().plot()
#Menambahkan Title and Axis Labels
'''
plt.title('Monthly GMV Year 2019') 
plt.xlabel('Order Month')
plt.ylabel('Total GMV')
'''
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue') #kustomisasi title dan axis labels
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()
#Kustomisasi Line dan Point
plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='D', linestyle='', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()
#kustomisasi grid
plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='x', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.grid(color='darkgray', linestyle=':',linewidth=0.5)
plt.show()
#kustomisasi axis ticks
fig=plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0) #mengatur batas bawah sb-y =0
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int)) #mengubah angka di sumbu y menjadi millyar
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red') #menambah informasi pada plot
plt.savefig('monthly_gmv.png', quality=95)
plt.show()