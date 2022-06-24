#zero division
a = int(input("Enter number"))
b =int(input("Enter number"))

try:
    c=a/b
except:
    print("Zero se divide nhi hota")
else:
    print(c)    