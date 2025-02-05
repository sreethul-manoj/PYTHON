# x=[1,2,3,4,5,6]
# y=x[::-1]
# print(y)

#using for loop

# x=[1,2,3,4,5,6]
# temp=[]
# for i in range(len(x)):
#     for j in range(i,(len(x))):
#         temp=x[i]
#         x[i]=x[j]
#         x[j]=temp
# print(x)
 

x=[1,2,3,4,5,6]
rev=[]
for i in range(len(x)-1,-1,-1):
    rev.append(x[i])
print(rev)


