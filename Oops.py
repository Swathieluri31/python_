# Oops.py
class Car:
    def __init__(self, color, brand):
        self.brand = brand
        self.color = color

    def Car_update(self, price, model):
        print(f" {price} rupees {model} model")

Car1 = Car("BMW","Red")
Car2 = Car("Audi","Blue")

print(Car1.brand)
print(Car2.color)

Car1.Car_update(5000000, "X5")
Car2.Car_update(6000000,  "Q7")

# mobile class
class Mobile:
    def __init__(self, style, color):
         self.style = style
         self.color = color
    
    def Mobile_update(self, year, company):
        print(f" {year}  {company} company")

Mobile1 = Mobile("Android", "red")
Mobile2 = Mobile("ios", "blue")

print(Mobile1.style)
print(Mobile2.color)

Mobile1.Mobile_update(2006, "samsung")
Mobile2.Mobile_update(2002, "motorola")

# class methods
class Car:
    wheels = 4
    @classmethod
    def update_wheels(cls, count):
        cls.wheels = count

Car.update_wheels(6)
print(Car.wheels)

#static method
class Car:
    @staticmethod
    def greet():
        print("Hello,Swathi")
Car.greet()

# write a python program to print only characters and numbers in a password without any special characters
def clean_password(password):
    cleaned = ''.join(char for char in password if char.isalnum())
    print("cleaned password:",cleaned)
clean_password("Swathi@031")

# Single Inheritance 
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greets(self):
        print("Hello from Child")
        
obj=Child()
obj.greet()
obj.greets()

# Multilevel Inheritance
class Grandparent:
    def greets(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greets(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

obj = Child()
obj.greets()


# Multiple Inheritance
class Father:
    def greet(self):
        print("Hello from Father")

class Mother:
    def greet(self):
        print("Hello from Mother")

class  Child(Father,Mother):
   pass

obj = Child()
obj.greet()

# Hierarchical Inheritance
class Parent:
    def greet(self):
         print("Hello from Parent")

class Child1(Parent):
    def c1(self):
         print("Hello from Child1")

class Child2(Parent):
    def c2(self):
         print("Hello from Child2")

obj1 = Child1()
obj2 = Child2()
obj1.greet()
obj1.c1()
obj2.greet()
obj2.c2()

# Polymorphism  it means many ways these are of 4 types 1.compile time polymorphism(Method Overloading) 2.Runtime polymorphism(Method Overriding) 3.Operator Overloading 4.Duck Typing

# Duck Typing
class Animal:
    def Sound(self):
       print("Animal Makes Sound")
class Dog:
    def Sound(self):
       print("Bark")
class Cat:
     def Sound(self):
        print("Meow")
def get_Sound(animal):
    animal.Sound()
get_Sound(Dog())
get_Sound(Cat())

# Overloading Method
class Science: 
    def add(self,a,b=0,c=0,d=0):
        return a+b+c
m=Science()
print(m.add(5,7,9))


   
