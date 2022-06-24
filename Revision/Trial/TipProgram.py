food = 20
name = input("Enter Name :")
age  = int(input("Enter Age:"))
food_name = input("Food to order :")
if age<18:
    tip_15 = food + food*0.15
    print("Your Bill ",tip_15)
else:
    tip_18 = food+food*0.18
    print("Your Bill ",tip_18)    
