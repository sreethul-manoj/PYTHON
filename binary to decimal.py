
X = input("Enter the binary number : ")
count = 0
A =X[::-1]
for i in range(len(A)):
    if A[i] == '1':
        count += 2 ** i

print(count)

