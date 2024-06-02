# arn = "arn:aws:iam::123456789012:user/sagar"

# print(arn.split("/")[1])

# name= arn

# print(name.upper())

# str1= "Hello"
# str2= "World"
# result= str1 +" "+str2

# print(result.upper())

# length= len(result)

# print("Length of the result is ", length)

# import re

# text = " Hey sagar how you doin?"
# pattern = r"you"

# match = re.match (pattern,text)

# if match:
#     print("Match found: ",match.group())

# else:
#     print("No match found")


# import time

# timestamp= time.strftime('%H:%M:%S')
# print(timestamp)

# hour = time.strftime('%H')
# print(hour)

# minute = time.strftime('%M')
# print(minute)

# second = time.strftime('%S')
# print(second)

import time

# timestamp= time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
#hour=int(input("Enter the time: "))

if hour>=0 and hour<12:
    print("Good Morning")
elif hour>=12 and hour <=17:
    print("Good afternoon")
elif hour >17 and hour <=24:
    print("Good Night")
         
