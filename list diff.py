x=[1,2,3,4,5]
y=[4,5,6,7,8]
z=x[:]
for i in z:
    for j in y:
        if i==j:
            x.remove(i)
print(x)