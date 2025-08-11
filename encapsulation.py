#public:
class student:
    def __init__(self):
        self.name="swathi"
obj=student()
print(obj.name)

#protect
class name:
    def __init__(self):
        self._age=20
obj=name()
print(obj._age)


#private
class name:
    def __init__(self):
        self.__grade="A"
obj=name()
print(obj._name__grade)

# get & set
class students:
    def __init__(self):
        self.__name=""

    def set_name(self,n):
        self.__name=n

    def get_name(self):
        return self.__name
s=students()
s.set_name("swathi")
print(s.get_name())

# Data abstraction
# its know as pillar of Oops it displays only main data and hides the implementation code
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is started")

    def stop(self):
        print("Car is stopped")
    def speed(self):
        print("Car speed")
    
    def cost(self):
        print("Car Cost")
 
class Bike(Vehicle):
    def start(self):
        print("Bike is started")

    def stop(self):
        print("Bike is stopped")

    def speed(self):
        print("Bike speed")
    
    def cost(self):
        print("Bike Cost")
 

#Creating object
c=Car()
c.start()
c.stop()
b=Bike()
b.speed()
b.cost()

# Animal abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
# subclass 1
class Dog(Animal):
    def sound(self):
        return "Bark"
# subclass 2
class Cat(Animal):
    def sound(self):
        return "Meows"

Animals=[Dog(), Cat()]
for a in Animals:
   print(a.sound())

# Payment gateway abstraction
from abc import ABC, abstractmethod
class Paymentgateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPayment(Paymentgateway):
    def pay(self, amount):
        print("Credited via Creditcard:")
    def refund(self, amount):
        print("Refunded via Creditcard:")
class UPI(Paymentgateway):
    def pay(self, amount):
        print("Credited via UPI:")
    def refund(self, amount):
        print("Refunded via UPI:")
# Creating objects
credit_card = CreditCardPayment()
credit_card.pay(1000)
credit_card.refund(500)
upi = UPI()
upi.pay(2000)
upi.refund(1000)
