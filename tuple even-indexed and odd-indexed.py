x=int(input("enter the range: "))
z=[]
for i in range(x):
    a=int(input("enter the elements : "))
    z.append(a)

odd=[]
even=[]
for i in range(len(z)):
    if i%2==0:
        even.append(z[i])
    else:
        odd.append(z[i])
print("odd intex :",odd)
print("even intex :",even)

  
