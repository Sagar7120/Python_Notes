star = int(input("Enter the number of starts you want to print = "))

for i in range (1, star+1):
    for j in range (1, i+1):
        print("*",end=" ")
    print()