x = int(input("Enter the range: "))
l = []
count = 0
count1 = 0

for i in range(x):
    a = int(input("Enter a number: "))
    l.append(a)

for i in l:
    if i % 2 == 0:
        count += 1
    else:
        count1 += 1

print("Even count in list: ", count)
print("Odd count in list: ", count1)
