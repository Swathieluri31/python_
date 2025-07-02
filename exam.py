#1 write a program to print the sum of the cubes of the numbers from M to N

M = int(input("Enter M:"))
N = int(input("Enter N:"))
total = 0
for i in range (M,N+1):
    cube = i**3
    total += cube
print(total)

 #2  Write a program that reads a distance D in km and calculates the total Score. 

d = int(input("Enter distance:"))
score = 0
bonus = 100
if d > 250: 
     score += (d-250)*10
     d=250
if d > 200: 
     score += (d-200)*8
     d=200
if d > 100:
     score += (d-100)*6
     d=100
if d > 50:
     score  += (d-50)*5 
     d=50
if d > 0:
     score += d*3
score += bonus
print(score)


#7) Write a function with the name show_numbers that takes a number n and print all the numbers 

n = int(input("Enter number:"))
for i in range (0,n+1):
             if i%2==0:
                   print(i,"EVEN") 
             else:
                   print(i,"ODD")

#8) Write a program that reads a string and prints the character of your string in reverse order.

n = input("Enter string:")
reverse = n[::-1]
for char in reverse:
       print(char)