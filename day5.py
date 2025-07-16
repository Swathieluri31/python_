# call by value
def modify(x):
    x = x+5
    print("Inside function:",x)
a = 10
modify(a)
print("outside function:")

def modify(x):
    x = x+5
    print("Inside function:",x)
a = 20
modify(a)
print("outside function:",a)

#call by reference
def add_item(my_list):
    my_list.append(99)
    print("Inside function:",my_list)

numbers = [1,2,3]
add_item(numbers)
print("Outside function:",numbers)

#lambda function
add = lambda a,b:a + b
print(add(10,20))

#No arguments
greet = lambda:"hello!"
print(greet())

#lambda with one argument
square = lambda x: x*x
print(square(6))

#lambda in a map() function
n = [1,2,3,4]
squares = list(map(lambda x: x**2,n))
print(squares)

#convert to uppercase
names = ['swathi','kavitha','vyshnav']
upper_names = list(map(str.upper,names))
print(upper_names)

#scope
def Hi():
    name = "Swathi"
    print("Hello",name)
Hi()
 
#built-in scope
x=[1,2,3,4,5]
print(len(x))
print(max(x))
print(min(x))