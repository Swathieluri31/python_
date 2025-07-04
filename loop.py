for i in range(5):
    print(i)

#break
for i in range(1, 10):
    if i == 3:
        break
    print(i)

#continue
for i in range(6):
    if i == 4:
       continue
    print(i)

#list
print("using list")

list=[10,20,30,40]
for i in list:
    print(i)

#list
list=["pooji","jyothi","vyshu","kavi"]
for i in list:
    print(i)

#even numbers
list =[1,2,3,4,5,6]
for i in list:
    if i%2 == 0:
        print(i)

#odd number
list = [1,2,3,4,5,6]
for i in list:
    if i%2 == 0:
        print(i)

#table 
for i in range(1,11):
    for j in range(1,11):
        print(i * j, end ="\t")
    print()

#while loop
count = 0
while count < 5:
    print(count)
    count += 1
