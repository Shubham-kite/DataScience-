import pandas as pd 
import matplotlib.pyplot as plt
dataset = pd.read_csv('data.csv')
print(dataset.corr())

''' graphical represntation '''
#dataset.plot(kind="line",x="Duration",y="Calories")
dataset.plot()
plt.show()