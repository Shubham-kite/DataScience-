import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

x=[45,13,42,78,12,4]
y=[12,18,24,36,40,46]
z=[1,2,3,4,5,6]
df = {
    'x':x,
    'y':y,
    'z':z
}
df = pd.DataFrame(df)
#print(df.corr())
sns.heatmap(df.corr())
