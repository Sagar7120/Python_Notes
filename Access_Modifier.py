#Public access modifier
#Private access modifier
#Protected access modifier

#Public
class Employee:
    def __init__(self):
        self.name = "Sagar"

a = Employee()
print(a.name)

#Private

class Employee:
    def __init__(self):
        self.__name = "Sagar"

a = Employee()
#print(a.__name)
print(a._Employee__name)
