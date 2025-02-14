x=[1,5,3,4,2,7]
max=0
z=set()
for i in range(len(x)):
    for j in range(len(x)):
        if i!=j:
            diff=x[i]-x[j]
            if diff>max:
                max=diff
                z.add(tuple(sorted((i,j))))
print(z)

     
        
        
    
