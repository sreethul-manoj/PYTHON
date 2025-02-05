x=int(input("enter the range : "))
l=[]
l2=[]
for i in range(x):
    a=input("enter the values : ")
    l.append(a)
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)


# for i in range(x):
#     if l[i] not in l2:
#         l2.append(l[i])