def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b

def revers(a):
    return a[::-1] 
def pal(a):
    if a==a[::-1]:
        return "palindrome"
    else:
        return "not"