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

#generate 2 multiples and and 3 multiples ?n may be negative or positive
n = int(input())

if n > 0:
    for i in range(1, n + 1):
        print(2 * i, 3 * i, end=" ")
else:
    print("Negative")

# Generate the given series if n is even generate even numbers and n is odd generate odd number
# Read input
n = int(input())

if n > 0:
    if n % 2 == 0:  # Even
        for i in range(2, n + 1, 2):
            print(i, end=" ")
    else:  # Odd
        for i in range(1, n + 1, 2):
            print(i, end=" ")
else:
    if n % 2 == 0:  # Negative even
        for i in range(-2, n - 1, -2):
            print(i, end=" ")
    else:  # Negative odd
        for i in range(-1, n - 1, -2):
            print(i, end=" ")

# if n is even generate even numbers and n is odd generate odd numbers
n = int(input())

# Positive number
if n > 0:
    if n % 2 == 0:  # Even
        for i in range(2, n + 1, 2):
            print(i, end=" ")
    else:  # Odd
        for i in range(1, n + 1, 2):
            print(i, end=" ")

# Negative number
else:
    if n % 2 == 0:  # Even
        for i in range(-2, n - 1, -2):
            print(i, end=" ")
    else:  # Odd
        for i in range(-1, n - 1, -2):
            print(i, end=" ")

# Generate table for the given number, n may be positive or negative
n = int(input())

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

#Generate the given series squares of the numbers till n
n = int(input())
if n > 0:
    for i in range(1, n + 1):
        print(i * i, end=" ")
else:
    print("No Series Generated")

# Generate even numbers in reverse order with in the ranges, n may be positive or negative
a = int(input())
b = int(input())

start = max(a, b)
end = min(a, b)
for i in range(start, end - 1, -1):
    if i % 2 == 0:
        print(i, end=" ")

# Find the number of digits in the given number
n = int(input())
abs_n = abs(n)
digit_count = len(str(abs_n))
print("Number of digits in the given number :", digit_count)

# Find the sum of the digits in the given number, n may be positive or negative
n = int(input())
abs_n = abs(n)
digit_sum = sum(int(digit) for digit in str(abs_n))
if n < 0:
    print("Sum is :", digit_sum)
else:
    print(digit_sum)

