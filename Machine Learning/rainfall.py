from scipy import stats
import matplotlib.pyplot as plt 
import numpy
x=[1,2,3,4,5]
y=[2,4,5,4,5]
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
