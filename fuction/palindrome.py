def palindrome(a):
    temp=""
    for i in a:
        temp=i+temp
    if a==temp:
        print("Its palindrome")
    else:
        print("Its not palindrome")
a=input("enter the string : ")
palindrome(a)

