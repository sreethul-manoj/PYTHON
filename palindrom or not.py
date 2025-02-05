x = int(input(" enter the range : "))
l = []
for i in range(x):
    a = input("enter the list : ")
    l.append(a)
if l == l[::-1]:
    print("it palindrome ")
else:
    print("it not palindrome ")
