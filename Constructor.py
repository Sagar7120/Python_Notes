class Person:
    def __init__ (self, n, a, o):
        self.name = n
        self.age = a
        self.occupation = o
    # def info(self):
    #     print(f"Hey {self.name}, age is {self.age} and occupation is {self.occupation}")


a = Person("Sagar", 24, "Developer")
print(f"Hey {a.name}, age is {a.age} and occupation is {a.occupation}")