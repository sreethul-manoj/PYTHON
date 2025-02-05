x=(1,2,3,4,5)
z=list(x)
rev=[]
for i in range(len(z)):
    rev= [z[i]] + rev
print(rev)
    
