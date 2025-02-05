x = [1, 2, 3, 4, 5, 6]
y = [3, 4, 5, 6, 7, 8]
l = []
for i in x:
    if i not in y:
        l.append(i)
print(l)
