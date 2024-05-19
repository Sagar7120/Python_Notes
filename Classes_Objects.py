class Person:
    name = "Sagar"
    age = 24
    occupation = "Developer"
    def info(self):
        print(f"Hey {self.name}, Your age is {self.age} and your occupation is {self.occupation}")

a= Person()
b = Person()
a.name = "Shubham"
a.age = 30
a.occupation = "HR"

b.name = "Neha"
b.age = 26
b.occupation = "Accountant"
print(Person())
a.info()
b.info()