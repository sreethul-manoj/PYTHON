x={1,2,3,4}
y={3,4,5,6}
z=set()
for i in x:
    if i not in y:
        z.add(i)
for i in y:
    if i not in x:
        z.add(i)
print(z)