import random
life = 3
result = random.randint(0,30)
while(life>0):
    user = int(input("Enter Your Guess between 1 to 30 :"))
    if(result==user):
        print("You Win !")
        break
    else:
        life = life - 1

if(life==0):
    print("Answer was ",result,"\nGame Over !")
