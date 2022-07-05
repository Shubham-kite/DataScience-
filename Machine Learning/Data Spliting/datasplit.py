<<<<<<< HEAD
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#loading data
data = pd.read_csv('car.csv')
#data information
print(data.info())
print(data.corr())
#spliting data
x=data[['Milege','Age']]
y=data['sellingPrice']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
#print(x_train)
#print(len(x_train))

#fiting 
reg = LinearRegression()
reg.fit(x_train,y_train)

#testing
print(reg.predict(x_test))
print(y_test)
=======
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#loading data
data = pd.read_csv('car.csv')
#data information
print(data.info())
print(data.corr())
#spliting data
x=data[['Milege','Age']]
y=data['sellingPrice']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
#print(x_train)
#print(len(x_train))

#fiting 
reg = LinearRegression()
reg.fit(x_train,y_train)

#testing
print(reg.predict(x_test))
print(y_test)
>>>>>>> 0e9b899331d70eb44d8c15c154f209f0853afb06
print("Accuraccy :",reg.score(x_test,y_test))