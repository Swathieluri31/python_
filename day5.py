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