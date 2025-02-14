def prime(a):
    if a>=1:
        flag=1
    for i in range(2,a//2+1):
        if a%i==0:
            flag=0
            return "not prime number"
    if flag==1:
        return "it's prime number"

    

