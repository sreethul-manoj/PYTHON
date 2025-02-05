x=[1,5,3,4,5,3,1,2,3,5]
result=[]
for i in x:
    if i not in result:
        result.append(i)
print(result)