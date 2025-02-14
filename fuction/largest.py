def largest(a):
    temp=0
    for i in a:
        if i>=temp:
            temp=i
    print(temp)
a=[1,2,3,4,5,6]
largest(a)