import pandas as pd 
import matplotlib.pyplot as plt 
player = ['a','b','c','d']
score =[350,650,453,235]
data ={
    'player': player,
    'score':score
}
dataset = pd.DataFrame(data)
plt.title("Scorecard")
plt.xlabel("Player")
plt.ylabel("Score")
plt.bar(dataset['player'],dataset['score'])
plt.show()
#print(dataset)