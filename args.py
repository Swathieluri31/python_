#args
def greet(*args):
   for name in args:
        print("Hello",name)
greet("Swathi","kavitha")

#args items
def show(*args):
   for item in args:
       print(item)

#kwargs
def func(**kwargs):
    for key,value in kwargs.items():
     print(f"{key} = {value}")

#recursion
def X(n):
    if n==0:
        print("Hello off!")
        return
    print(n)
    X(n-1)
    
#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(6))