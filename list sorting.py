x=[13,2,3,4,3,1,5,7,6,0,9,7,10]
for i in range(len(x)):
    for j in range(i,(len(x))):
        if x[i]>x[j]:
            # x[i],x[j]=x[j],x[i]
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)

   