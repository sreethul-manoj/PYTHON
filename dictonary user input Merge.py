# x=int(input("enter the range : "))
# d={}
# for i in range(x):
#     key=input("enter the key : ")
#     values=input("enter the values : ")
#     d[key]=values
# print(d)

# d={'fgf':2,'tryt':6,'gffh':5}
# print(d['gffh'])
# d['abcd']=7                    #key-value pair
# print(d)


# x={}                          #remove key
# for key in d:
#     if key!="fgf":
#         x[key]=d[key]
# print(x)

# x={"a":1,"b":2,"c":3}        #print values&keys
# print(x.keys())
# print(x.values())
# print(x.items())



x={"a":1,"b":2,"c":3}           #Merge two dictionaries 
y={"n":1,"e":2,"l":3}
e= {**x,**y}
print(e)