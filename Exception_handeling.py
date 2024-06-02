# a = input("Enter the numbers: ")

# print (f"Multiplication of the {a} is:-")

# try:
#     for i in range (1,11):
#         print (f"{int(a)} X {i} = {int(a)*i}")

# except:
#     print("Invalid input")

# print("End of the program")


# try:
#     num = int(input("Enter the number: "))
#     a= [1,10,60]
#     print(a[num])

# except ValueError:
#     print("The number is not in correct datatype")

# except IndexError:
#     print("The index is not present in the list")


# a= int(input("Enter the value between 5 and 10: "))

# if a<5 or a>10:
#     raise ValueError("The value is not valid")
# else:
#     print("The value is correct: ",a)

# 0 1 1 2 3 5 8

def Fibonacci(n):

    if n < 0:
        print ("Incorrect")

    elif n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
print(Fibonacci(15))


