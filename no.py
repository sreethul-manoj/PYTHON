x=[1,2,3,4,5,6,7,8,9,5,5,6,5,3,4,5,5,5]
y=int(input("enter the number : "))
count=0
for i in x:
    if i==y:
        count+=1
print("count=",count)

