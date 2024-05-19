class Myclass:
    def value (self, name, age, password):
        self.name = name
        self._age = age       #private data
        self._password = password    #private data

    #Getter method
    def getter(self):
        print (f"Getting getter {self.name}, {self._age}, {self._password}")
        return self._age
    
    #Setter Method
    def setter(self, x):
        print ("Getting setter")
        self._age = x

val = Myclass("Sagar", 24, 123)
val.setter(10)
print(val.getter())

class Geeks: 
     def __init__(self): 
          self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self._age = a 
  
mark = Geeks() 
mark.age = 19
  