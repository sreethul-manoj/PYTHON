# A=input("enter the char : ")
# if A==A[::-1]:
#     print(A,"is palindrome")
# else:print(A,"is not palindrome")


A=input("enter the char : ")
S=""
for i in A:
    S=i+S
if S==A:
    print(A,"is palindrome")
else:print(A,"is not palindrome")