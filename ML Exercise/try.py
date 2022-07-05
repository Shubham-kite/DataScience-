from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('income.csv')
print(df.info())

x=[[df.year]]
y=df.incomes

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8)