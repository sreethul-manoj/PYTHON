# file=open("file exp.txt","x")

# file=open("file exp.txt","w")
# file.write("Hello World!!")
# file.close()

# file=open("file exp.txt","a")
# file.write(" Hai Sreethul !!")
# file.close()

# file=open("file exp.txt","r")
# print(file.read())

import os
if os.path.exists("file exp.txt"):
    os.remove("file exp.txt")
    print("removed")
