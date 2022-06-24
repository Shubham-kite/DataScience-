import matplotlib.pyplot as plt 
import pandas as pd 
plt.title("player score")
ing = ['ing1','ing2','ing3','ing4','ing5']
r_score=[34,56,23,130,45]
v_score=[56,65,5,100,33]
Rohit_data={
    'ing':ing,
    'score':r_score
}
Virat_data={
    'ing':ing,
    'score':v_score
}
Rohit = pd.DataFrame(Rohit_data)
Virat = pd.DataFrame(Virat_data)
#print(Rohit)
#print(Virat)
'''rohit details '''
plt.subplot(1,2,1)
plt.title("Rohit Scorecard")
plt.bar(Rohit['ing'],Rohit['score'])


''' virat details '''
plt.subplot(1,2,2)
plt.title("Virat Scorecard")
plt.bar(Virat['ing'],Virat['score'])
plt.show()
