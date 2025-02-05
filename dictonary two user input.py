x=int(input("enter the range_of_outer key : "))
d={}
for i in range(x):
    outer_key=input("enter the outer_key : ")
    range_inner_key=int(input("enter the inner_key range : "))
    d1={}
    for i in range(range_inner_key):
        inner_key=input("enter the inner key :")
        inner_values=input("enter the inner values :")
        d1[inner_key]=inner_values
    d[outer_key]=d1
print(d)