# Map
def cube(x):
    return x * x * x

nlist = [1,3,5,6,7,8,9]
cubelist = list(map(cube, nlist))
print(cubelist)
print(type(cubelist))

#filter

def filter_fun(a):
    return a>5

newlist = list(filter(filter_fun, nlist))
print(newlist)