from scipy import stats
import matplotlib.pyplot as plt 
import numpy
import pandas as pd

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y=[713.35,728.50,739.80,748.50,752.85,752.65,749.75,744.30,746.75,735.25,729.50,732.75,720,688,685.50,687.25,678.50,686.85,685.95,696.10,686.60,699.15]
''' y= mx+c'''
slope,intercept,r,p,std_err=stats.linregress(x,y)

def mymodel(x):
    return slope*x+intercept

x_value = int(input("Enter value to predict :"))
x.append(x_value)
prediction = mymodel(x_value)
print(prediction)
plt.title("Rainfall")
plt.xlabel("input variale")
plt.ylabel("dependent variable")
y.append(prediction)
plt.plot(x,y,marker="o",color="green")
plt.show()
