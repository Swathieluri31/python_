#break it is used to modify the behaviour
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
for i in range(5):
    if i==2:
        continue
    print(i)

#break on 7
for i in range(1,11):
    if i == 7:
        break
    print(i)

#continue to skip 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#break on user input 'exit'
while True:
    a = input("type someything:")
    if a == 'exit':
        break
    print("you typed:",a)

while True:
    password = str(input("Enter your password:")) 
    if password == 'swathi':
        break
    print(password)

#skip negative numbers
n = [4, -1, 7, -3, 0, 9]
for num in n:
    if num < 0:
        continue
    print(num)

#stop printing characters on space
text ="Hello World"
for char in text:
    if char ==' ':
       break
    print(char)

#skip vowels
text = "education"
vowels = "aeiou"
for char in text:
    if char in vowels:
        continue
    print(char)

#break on first number > 20
n = [5,10,15,25,30]
for num in n:
    if num > 20:
        break
    print(num)
    
# continue even numbers
for i in range(1 , 21):
    if i % 2 == 0:
        continue
    print(i)

# break in while loop
i = 1
while True:
    if i == 8:
        break
    print(i)
    i += 1

# continue in while loop
i = 0
while i < 10:
    i += 1 
    if i == 3 or i == 6:
        continue
    print(i)

#break if total sum > 100
n = [10, 20, 30, 40, 15, 5, 7]
total = 0
for num in n:
    total += num
    if total > 100:
        break
    print("sum:",total)

#skip words starting with b
String = ["bat","apple","banana","cat","dog"]
for word in String:
    if word.startswith('b'):
        continue
    print(word)

#nested loop with break
for i in range(1,4): 
     for j in range(1,10):
         if i*j > 20:
             break
         print(f"{i}x{j}= {i*j}")

#find first even and break
nums = [1, 3, 5, 8, 9]
for num in  nums:
    if num % 2 == 0:
        print("First even:",num)
        break

#continue on divisible by 4 or 6
for i in range(1, 31):
    if i%4 == 0 or i%6 == 0:
        continue
    print(i)

#skip every third caharacter
text = "abcdefghij"
for index, char in enumerate(text, 1):
if index %3 == 0:
    continue
print(char)


