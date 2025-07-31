#try
try:
    result=10/0
except ZeroDivisionError:
      print("Error:Arithmetic exception")

# Product of array except self
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output

#try
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError;
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")

#file handling
try:
    fileptr = open("file.txt", "r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")

#
class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)

