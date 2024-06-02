# def initialMean (a,b):
#     mean = (a*b)/(a+b)
#     print (mean)

# a=5
# b=8
# initialMean(a,b)

# def name (fname, lname ):
#     print ("Sagar is friend of", fname ,"and", lname)

# name("aniket", "utkarsh")

# def compare (a,b):
#     if (a>b):
#         print("First value is greater")
#     else:
#         print("Second value is greater")

# compare(20,10)

def average (*number):
    sum = 0
    print (type(number))
    for i in number:
        sum = sum + i
    print ("Average of the number is :", sum / len(number))

average(5,7)

def name (**name):
    print(type(name))
    print (" My name is ", name["fname"],name ["lname"] ,name ["sname"])

name (fname= "Sagar", lname= "Kailas", sname = "shelki")

