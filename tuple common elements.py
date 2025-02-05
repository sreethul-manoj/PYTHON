x=(1,2,3,4,5,6,7,8)
y=(4,5,6,7,8)
P=[]
for i in x:
    for j in y:
        if i==j:
            P.append(i)
print(P)