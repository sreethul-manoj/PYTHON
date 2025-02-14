x = int(input("enter the range: "))
l = []
for i in range(x):
    a = int(input("enter the list: "))
    l.append(a)
print(l)


target = int(input("enter the target: "))
z = set()

for i in range(len(l)):
    for j in range(i + 1, len(l)):  
        if l[i] % 2 == 0 and l[j] % 2 == 0:  
            if l[i] * l[j] == target:
                pair = tuple(sorted((i, j)))
                z.add(pair)
                

print(z)