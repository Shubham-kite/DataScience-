import random
import time
import csv
import matplotlib.pyplot as plt

''' requirement setup '''
sec_3=0
sec_6 =0
sec_10 = 0
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
w1 = word[random.randint(0,25)]
w2 = word[random.randint(0,25)]
w3 = word[random.randint(0,25)]
string = w1+w2+w3
number = random.randint(1,120)
sub = random.randint(5,13)
print(string)
print(number)
''' for the 3 second '''
#for 3 sec
#time.sleep(3)
for i in range(random.randint(0,8)):
    time.sleep(1)
    number = number-sub
    print(number)

user_input0= input("Enter String which is display previously : ")
if(string == user_input0):
    sec_3 = sec_3 + 1
#for 6 sec
time.sleep(2)
for i in range(random.randint(3,10)):
    time.sleep(1.5)
    number = number-sub
    print(number)

user_input1= input("Enter String which is display previously : ")
if(string == user_input1):
    sec_6 = sec_6 + 1


#for 10 sec
time.sleep(2)
for i in range(random.randint(3,15)):
    time.sleep(2)
    number = number-sub
    print(number)

user_input2= input("Enter String which is display previously : ")
if(string == user_input2):
    sec_10 = sec_10 + 1    

print("3 second score ",sec_3)
print("6 second score ",sec_6)
print("10 second score ",sec_10)

list1 = [3 ,6,10]
list2 =[]
list2.append(sec_3)
list2.append(sec_6)
list2.append(sec_10)
plt.plot(list1,list2)
fig,ax = plt.subplots()
ax.set_ylabel('Score')
ax.set_xlabel('time')
plt.show()

#data = dict(zip(list1,list2))
#print(data)