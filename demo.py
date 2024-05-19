# stnew = "gfdSagarsjhdgikshf"
# new = stnew[3:-10]
# print(new)
# stnew = new[-1] + new[:-1]
# print(stnew)

# def cube(x):
#     return x*x*x

# print(cube(2))

# nlist = [1,2,4,5,6,7,9]

# cubelist = list(map(lambda x: x*x*x, nlist))
# print(cubelist)

st = "sagar what is your name 8lw_bt jkhdskfh ksdhf kjsdhf skdjfh"

list = ["1lw_bt","2lw_bt","3lw_bt","4lw_bt","5lw_bt","6lw_bt","7lw_bt","8lw_bt"]

def find(st):
    for i in list:
        if i in st:
            return i
           
    else:
        print("No word found")

print(find(st))