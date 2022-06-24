num1 = int(input("\nEnter Number :"))
num2 = int(input("\nEnter Number :"))
print("\n1.Add \n2.Sub \n3.Multiplication \n4.Divison \n0.Exit")
ch = int(input("Enter Your Choice :"))
while(ch!=0):
    print("\n1.Add \n2.Sub \n3.Multiplication \n4.Divison \n0.Exit")
    ch = int(input("Enter Your Choice :"))
    if(ch==1):
        print("Addition is ",num1+num2)
    elif(ch==2):
        if(num1>num2):
            print("Subtraction is ",num1-num2)
        else:
            print("Subtraction is ",num2-num1)
    elif(ch==3):
        print("Multiplication is ",num1*num2)
    elif(ch==4):
        print("Divison is ",num1/num2)

