x=(1,2,0,3,6,4,5)
z=list(x)
max=z[0]
min=z[0]
for i in z:
    if i < min:
        min=i
    if i > max:
        max=i
print(max,min)
  