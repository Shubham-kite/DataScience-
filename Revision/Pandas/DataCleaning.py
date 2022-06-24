import pandas as pd 
dataset = pd.read_csv('dirtydata.csv')
#information about data 
print(dataset.info())
#printing whole data


''' filling blank data using fillna '''
x = dataset['Calories'].mean()
dataset['Calories'].fillna(x,inplace=True)


''' to change the formate of datatype '''
dataset['Date'] = pd.to_datetime(dataset['Date'])


''' replace wrong data '''
for i in dataset.index:
    if(dataset.loc[i,'Duration']>60):
        dataset.loc[i,'Duration']=60
print(dataset.to_string())