x=[1, 2, 2, 3, 4, 4, 5]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)