x=input("enter the string : ")
y=x.split(" ")
temp=" "
for i in range(len(y)):
    a=y[i]
    b=a[0].upper()+a[1:]
    temp+=b+" "
print(temp)
    