#uppercase
a = "kiet"
print(a.upper())

#lowercase
a = "KIET"
print(a.lower())

#remove space
a = "kiet"
print(a.replace('t','k'))

# slicing
#syntax : string[start:end:step]
#slicing
s="kiet students"
print(s[0:5])
print(s[1::])
print(s[:5:])
print(s[::2])
print(s[1:9:2])

#reverse
s="python"
print(s[-1::])
print(s[:-3:])
print(s[::-1])
print(s[-1:-5:-1])
 
s="kietwcollegestudents"
print(s[::-1])

#list slicing in python is a way to extract a portion(sublist)from a list
#syntax list[start:stop:step]
list = [10,20,30,40,50,60]
print(list[1:3:1])

 #list methods
 #append
list=[10,20,30]
list.append([40,50])
print(list)

#extend
list=[10,20,30]  
list.extend([40,50])
print(list)

#insert
list=[10,20,30] 
list.insert(1,50)
print(list)

#remove
list=[10,20,30] 
list.remove(30)
print(list)

#index
list=[10,20,30]
x=list.index(30)
print(x)

#pop
list=[10,20,30]
list.pop()
print(list)

#clear
list=[10,20,30]
list.clear()
print(list)

#count
list=[10,20,30,40,50,60,30,80]
x=list.count(30)
print(x)

#sort
list=[90,70,80,50,60]
list.sort()
print(list)

#reverse
list=[90,70,60,80,50,30,77]
list.reverse()

#copy
list=[10,20,30]
x=list.copy()
print(x)

