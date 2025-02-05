temp=float(input("enter the temp : "))
if temp<=0:
    print(temp,"is cold")
elif 0<temp<=15:
    print(temp,"cool")
elif 15<temp<=30:
    print(temp,"warm")
else:print(temp,"hot")