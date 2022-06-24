import pandas as pd 
data = {
    'mycar':['BMW','Tesala','Tata','MG'],
    'type':['Petrol','EV','EV','EV']
}
data = pd.DataFrame(data,index=[1,2,3,4])
#print(data)
Scorecard ={
    'Rohit':120,'Rahul':32,'Kolhli':83
}
score = pd.Series(Scorecard)
#print(score)

#player 
Scorecard ={
    'player' :['Rohit','Virat','Surya','Pandya','Rishab','Dk','RJ','Bk','Chahal','Boom','Shami'],
    'score':[67,33,45,12,45,22,78,'NULL','NULL','NULL','NULL']
}
Scorecard = pd.DataFrame(Scorecard)
print(Scorecard)
print(Scorecard.loc[[5]])