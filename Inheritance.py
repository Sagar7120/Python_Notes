#Parent class
class Employee:
    def __init__(self, name, emp_id, grade):
        self.name = name
        self.emp_id = emp_id
        self.grade = grade

    def show (self):
        return self.name, self.emp_id, self.grade

#e = Employee("Sagar", 2223212, "C1")
#e.show()
#Child class
class Programming(Employee):

    #Constructor
    def __init__ (self, name, emp_id, grade, lang):
        Employee.__init__(self, name, emp_id, grade)
        self.lang = lang

    

    def showlang(self):
        print (f"The name is {self.name}, employee id is {self.emp_id} and Grade is {self.grade}. The known laungage of the  employee is {self.lang}")

#SubClass
class Role(Programming):
    def __init__(self, name, emp_id, grade, lang, role):
        Programming.__init__(self, name, emp_id, grade, lang)
        self.role = role

    def call(self):
        print (f"The name is {self.name}, employee id is {self.emp_id} and Grade is {self.grade}. The known laungage of the  employee is {self.lang} and the role is {self.role}")

details = Role("Sagar", 2223212, "C1","Python", "Developer")
details.call()
