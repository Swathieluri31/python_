#sum of list elements
list=[3,5,2,8]
x=sum(list)
print("Sum:",x)  #Sum : 18

#type conversion(list to tuple)
list=['apple','banana','mango']
x=tuple(list)
print("Tuple:",x) #Tuple: ('apple', 'banana', 'mango')

#Take a tuple of numbers and print maximum and minimum values
tuple=(4,7,1,9,3)
x=max(tuple)
y=min(tuple)
print("maximum:",x) # maximum: 9
print("minimum:",y) # minimum: 1

#Given a list of 6 elements,print first and last element slice of elements from index 1 to 4
list=[10,20,30,40,50,60]
print("First:",list[0]) # First: 10
print("Last:",list[-1]) # Last: 60
print("slice[1;5]:",list[1:5]) # slice[1;5]: [20, 30, 40, 50] 

#Write a program to count how many times a specific element appears in a tuple
Tuple = (1,2,3,2,4,2,5)
x=Tuple.count(2)
print("Count 0f 2:",x) # Count 0f 2: 3

#append
a = [1,2,3]
b = a
b.append(4)
print(a) #[1, 2, 3, 4]

# change of values
x = [1,2,3]
y = x[:]
y[0] = 100
print(x) # [1, 2, 3]
print(y) # [100, 2, 3]

# result 
list = [1,2,3,4,5]
print(list[1:4])
 
#list
list = [i for i in range(5)]
list[2:4] = [10,11,12]
print(list) # [0, 1, 10, 11, 12, 4]

# list ->> tuple
fruits = ['apple','banana','cherry']

print(fruit_tuple)
 
#append
numbers = [1,2,3]
numbers.append(4)
print(numbers)