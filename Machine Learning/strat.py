import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats
import numpy as np
import pandas as pd 
x=[1,2,3,4,6]
y=[2,4,6,8,12]
plt.xlabel("Time")
plt.ylabel("Price")
slope,intercept,r,p,std_err = stats.linregress(x,y)
def linear(x):
    return slope *x + intercept  


num_list = []
pre_value = float(input("Enter previous close :"))
pre_value = int(pre_value)
x.append(pre_value)
pre_value = float(pre_value)        
value = linear(pre_value)
y.append(value)
print(value)
pre_sqrt = pre_value**0.5
num = round(pre_sqrt)
print(num)
if(num%2==0):
    new_pre  = num-1 
    new_next = num+1

if(num%2!=0):
    new_next = num+2
    new_pre  = num-2

print("new_previous ",new_pre,"new_next",new_next)

sqr_pre = new_pre**2
sqr_next = new_next**2

print("square of next ",sqr_next ,"square of previous",sqr_pre)

for i in range(sqr_pre,sqr_next+1):
    #print(i)
    num_list.append(i)
support = num_list[0]
median  = np.median(num_list)
res     = num_list[-1]
print("support :",num_list[0])
print("median :",np.median(num_list))
print("resistance :",num_list[-1])

if(value< res and value>support):
    print("You can buy this stock")
elif(value>res):
    print("wait to buy")
else:
    print("wait and watch")

point =[]
point.insert(0,support)
point.append(median)
point.append(res)
#point.append(value)

z = point
label=['Support','Median','Resistance']
#plt.legend()
plt.plot(x,y,marker="*")
plt.barh(z,width=value,height=0.1,color="red")
#plt.(z)
plt.show()