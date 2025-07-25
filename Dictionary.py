#Dictionary is a collection of key-value pairs where we can acess the values using its keys.
#It is mutable(changes can be made)
a={1:"a"}
print(type(a))

d={1:"mn",2:"abc",34:890,"ab":"cd","ef":234}
print(d[1])

#key
n = int(input("Enter number of items: "))
d={}
for i in range(n):
    key = input("Enter key: ")
    val = input("Enter value: ")
    d[key] = val
print(d)

#update
d={1:"mn",2:"abc",34:890,"ab":"cd","ef":234}
d.update({1:'abc',2:451})
print(d)

#get
d={1:"mn",2:"abc",34:890,"ab":"cd","ef":234}
print(d.get(34))

#copy
d={1:"mn",2:"abc",34:890,"ab":"cd","ef":234}
d1 = d.copy()
print(d1)

#pop
d={1:"mn",2:"abc",34:890,"ab":"cd","ef":234}
print(d.pop(34))
print(d)
print(d.popitem())
print(d)

#Squares Dictionary
n = map(int, input("Enter a value: ").split())
square_dict = {x: x**2 for x in n}
print(square_dict)