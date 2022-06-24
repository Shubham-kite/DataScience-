class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Wish you very happy b'day ",self.name,'you are now ',self.age+1 ,'years old')
    
class student(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def enroll(self):
        print(name,'are enroll as a student')






name = input("Enter name :")
age  = int (input("Enter age :"))
wish = Person(name,age)
a = student(name,age)
a.enroll()
a.greet()
