import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('TATAMotors.csv')
x= dataset[['p_close']]
y=dataset['n_close']

reg = LinearRegression()

x_test,x_train,y_train,y_test = train_test_split(x,y,test_size=0.2)

#reg.fit(x_train,y_train)
reg.fit(dataset[['p_close']].values,dataset['n_close'].values)

print(reg.predict([[412.7]]))
print(reg.score(dataset[['p_close']].values,dataset['n_close'].values))
