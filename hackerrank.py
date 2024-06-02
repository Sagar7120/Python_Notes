'''n = int(input("Enter the number:- "))

if n % 2 != 0:
    print("Weird")
    
elif n % 2 == 0:
    if (n>2) and (n<5):
        print("Not Weird")

    elif (n>6) and (n<20):
        print ("Weird")

    elif (n>20):
        print("Not Weird")

'''

'''n = int(input())
    
for i in range (n):
    i = i**2
    print(i)'''

'''n = int(input())
    
for i in range(1,n+1):
   print(i,end='')'''

'''s = "Hello" [::-1]
print(s)


a= 10000
b= 1000
print("a") if a>b else print ("=") if (a==b) else print ("B")'''

# 0 1 1 2 3 5 8 13

def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    
print(fibonacci(0))
