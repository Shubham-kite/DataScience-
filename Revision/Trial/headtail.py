import random
head = 0
tail = 0
for i in range(100):
    guess = random.randint(0,1)
    if(guess==1):
        head = head+1
    else:
        tail = tail +1

print("head count is :",head ,"Tail count is ",tail)
