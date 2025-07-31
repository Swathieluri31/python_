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