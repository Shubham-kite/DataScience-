import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats 
''' regression => y= mx+c '''
''' 
   m = slope
   x = input var
   c = intersecpt
   '''

x=[1,2,3,4,6]
y=[2,4,6,8,12]
slope,intercept,r,p,std_err = stats.linregress(x,y)

def linear(x):
    return slope *x + intercept
value = linear(17)
print(value)
  
visual = list(map(linear,x))
plt.scatter(x, y)
plt.plot(x,visual)
plt.show()