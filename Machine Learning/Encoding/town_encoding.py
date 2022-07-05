import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
#through dummy col method 
df = pd.read_csv('town_wise.csv')
dummies = pd.get_dummies(df)
new_df = pd.concat([df,dummies],axis='columns')
new_df = new_df.drop(['town'],axis='columns')

reg = LinearRegression()
x=new_df[['area','town_banglore','town_mumbai','town_pune']]
y=new_df['price']

reg.fit(x.values,y.values)
#print(new_df)
#print("for pune :",reg.predict([[710,0,0,0,1]]))

#using label encoder
encode = LabelEncoder()
df.town = encode.fit_transform(df.town)

print(df)
