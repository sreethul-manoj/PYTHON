x={
    "name":"sreethul",
    "age":"24",
    "Dob":"2001"
}
x["dob"]=2000 #change
x.update({"name":"amal"}) #update
print(x)
print(x.keys())
print(x.values())
print(x.items())
print(x["name"])
print(x["dob"])

#User input
x=int(input("enter the range : "))
d={}
for i in range(x):
    key=input("enter the keys : ")
    values=input("enter the values : ")
    d[key]=values
print(d)
    