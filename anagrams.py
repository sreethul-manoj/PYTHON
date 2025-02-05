A=input("enter the first string : ")
B=input("enter the second string : ")
flag=1
if len(A)==len(B):
    for i in A:
        if A.count(i)!=B.count(i):
            flag=0
            break
else:
    flag=0
if flag==1:
    print("its anagrams")
else:
    print("not")