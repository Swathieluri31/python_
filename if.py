x = 10
if x > 5:
    print("x is greater than 5")

#Checking if a number is positive
number = int(input("Enter a number:")) 
if number > 0:
    print("The number is positive.")

# Check if number is divisible by both 3 and 5
number = 30
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")

#check if number is divisible by both 2 and 8
number = int(input("Enter a number"))
if number % 2 == 0 and number % 8 == 0:
    print("Divisible ny both 2 and 8")

x = 3
if x > 5:
    print("x is greaterthan 5")
else:
    print("x is 5 or less")

#positive & negative
x = -2
if x > 0:
    print("the number is positive")
else:
    print("the number is negative")

#even or odd
x = 10
if x % 2 == 0:
    print("even")
else:
    print("odd")

#check if a person is eligible for voting
age = int(input("Enter your age:"))
if age >= 18:
    print("Is eligible")
else:
    print("Not eligible")

#find the largest of two numbers
a = int(input("Enter a number:"))
b = int(input("Enter b number:"))
if a > b:
    print("a is greater")
else:
    print("b is greater")

#checking vowels
ch = 'e'
if ch in 'aeiouAEIOU':
    print("vowels")
else:
    print("consonants")

#checking password
password = "Swathi"
if password == "Swathi":
    print("Valid")
else:
   print("Invalid")   
         
#checking leap year or not
n = int(input("enter year:"))
if n%4 == 0 or n%400 == 0 or n%100 != 0:
    print("leapyear")
else:
    print("not leapyear")

#Check the great number among a,b,c
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c :
    print("a is greater")
elif b > a and b > c :
    print("b is greater")
else:
    print("c is greater")


     
