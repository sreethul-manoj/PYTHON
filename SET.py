#Dupicate
# x={"apple","banana","apple","kiwi"}
# print(x)

#Add
# x={"banana","kiwi"}
# x.add("apple")
# print(x)

# x={"apple","banana"}
# y={"kiwi","orange"}
# x.update(y)
# print(x)

#Remove
# x={"apple","kiwi","banana"}
# x.remove("banana")
# print(x)

# x={"apple","banana","kiwi"}
# x.discard("banana")
# print(x)

#Two set
# x={5,6,7,8}
# y={1,2,3,4}
# z=x.union(y)
# print(z)

x={1,2,3}
y={4,5,6}
z={7,8,9}
w=x|y|z
print(w)