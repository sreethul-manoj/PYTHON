x=input("enter the string : ")
str=""
for i in x:
    if i in "1234567890":
        str+=i
print(str)