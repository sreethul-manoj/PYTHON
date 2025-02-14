x=input("enter the string : ")
d={}
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
for key in d:
    l.append(d[key])
ans=True
first_value=l[0]
for i in l:
    if i!=first_value:
        ans=False
        print("false")
        break
if ans==True:
    print("true")
          

