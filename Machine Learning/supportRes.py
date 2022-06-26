import numpy as np  
num_list = []
pre_value = float(input("Enter previous close :"))
pre_sqrt = pre_value**0.5
num = round(pre_sqrt)
print(num)
if(num%2==0):
    new_pre  = num-1 
    new_next = num+1

if(num%2!=0):
    new_next = num+2
    new_pre  = num-2

print("new_previous ",new_pre,"new_next",new_next)

sqr_pre = new_pre**2
sqr_next = new_next**2

print("square of next ",sqr_next ,"square of previous",sqr_pre)

for i in range(sqr_pre,sqr_next+1):
    #print(i)
    num_list.append(i)
print("support :",num_list[0])
print("median :",np.median(num_list))
print("resistance :",num_list[-1])
