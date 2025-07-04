#Generate even numbers from 1 to n? read a number, number may be positive or negative
n = int(input())
if n > 0:
    for i in range(2, n+1, 2):
        print(i, end=" ")
else:
    for i in range(-2, n-1, -2):
        print(i, end=" ")

# Read two numbers from the user, generate 3 multiples with in the range ? number may be positive or negative
a = int(input())
b = int(input())

start = min(a, b)
end = max(a, b)

for i in range(start, end + 1):
    if i % 3 == 0:
        print(i, end=" ")

# Read a number from the user, generate numbers from 1 to n? n is number , it may be + or negative
n = int(input())
if n > 0:
    for i in range(1, n + 1):
        print(i, end=" ")
else:
    print("Negative")

# Read a number generate even numberS from 1 to n ?n may be +ve or -ve
n = int(input())

if n > 0:
    for i in range(2, n + 1, 2):
        print(i, end=" ")
else:
    for i in range(-2, n - 1, -2):
        print(i, end=" ")
    print(-1, end=" ")
