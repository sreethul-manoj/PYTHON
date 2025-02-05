# x=[1,2,3,4]
# tuple=tuple(x)
# print(tuple)


x=int(input("enter the ranage : "))
temp=[]
for i in range(x):
    a=input("enter the list : ")
    temp.append(a)
tuple=tuple(temp)
print(tuple)

print(tuple[2])

