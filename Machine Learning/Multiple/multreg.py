''' 
formula
    y = m1x1+m2x2+m3x3+c

'''
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
dataset= pd.read_csv('Raw Data.csv')

''' information about data '''
print(dataset.info())
print(dataset.corr())

''' plotting graphs'''
plt.suptitle("HousePricing")
plt.subplot(1,2,1) #no.row and no.col and which no of subplot
plt.title("HousePrice on basis of Area")
plt.ylabel("Price")
plt.xlabel("Area")
plt.scatter(dataset.Area,dataset.Price,color="red")
plt.plot(dataset.Area,dataset.Price)

plt.subplot(1,2,2)
plt.title("HousePrice on basis of Bedroom")
plt.xlabel("Bedroom")
plt.ylabel("Price")
plt.scatter(dataset.Type,dataset.Price,color="green")
plt.plot(dataset.Type,dataset.Price)

plt.show()

''' model training'''
reg = LinearRegression()
reg.fit(dataset[['Area','Type']].values,dataset.Price)

''' testing/Actual Execution'''
print(reg.predict([[420,2]]))
