x=input("enter a string : ")
digit=0
alpha=0
for i in x:
    if i in "1234567890":
        digit+=1
    elif i in "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM":
        alpha+=1
print("alpha count is ",alpha)
print("digit count is ",digit)
