#public:
class student:
    def __init__(self):
        self.name="swathi"
obj=student()
print(obj.name)

#protect
class name:
    def __init__(self):
        self._age=20
obj=name()
print(obj._age)


#private
class name:
    def __init__(self):
        self.__grade="A"
obj=name()
print(obj._name__grade)

# get & set
class students:
    def __init__(self):
        self.__name=""

    def set_name(self,n):
        self.__name=n

    def get_name(self):
        return self.__name
s=students()
s.set_name("swathi")
print(s.get_name())


