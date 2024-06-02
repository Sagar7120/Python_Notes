#list is mutable (changeable)
l = [20, 10, 5, "Sagar"]
l.append(50)
print(l)
l.insert(1,100)
print(l)

m= [900,200,4000]
l.extend(m)
print(l)
k= l+m
print(k)

tup= ("Spain", "Italy","India","England")
temp=list(tup)
print(type(temp), temp)
temp.append("Russia")
print(temp)
temp.pop(2)
print(temp)
temp[2]="Finland"
print(temp)

country=tuple(temp)

print(type(country), country)