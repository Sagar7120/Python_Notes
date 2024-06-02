# for i in range(1,15):
#     print ("5 x ", i,"= ", 5*i)
#     if (i==10):
#         break

# print("you are out of the loop")
########################################################################
# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))

# def calculate (a,b):
#     mean=(a*b)/(a+b)
#     print("The mean value of both numbers is :",mean)

# if (a>b): 
#     print("First number is greater")

# elif a==b:
#     print("Both numbers are same")

# else:
#     print("second number is greater")

# calculate(a,b)

# def avg(a=10, b= 20):
#     print ("the average of both numbers is: ", (a+b)/2)

# avg(a=60,b=90)
###############################################################
def avg (**numb):
    print(type(numb))
avg()

def name(fname, mname="Sagar", lname="Ved"):
    print("hello, ",fname, mname," and ",lname)

name("mahesh","vaibhav")

def avg (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

print(avg(101,15))

###############################################################

# list1= [10, "Sagar", 50]
# print(list1)
# print(type(list1))
# print(list1[1])

