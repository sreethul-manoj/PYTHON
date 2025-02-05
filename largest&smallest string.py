x = [1, 99999, 3, 4, 5, 6, 100, 8, 10, 10]
largest=x[0]
smallest=x[0]
for i in range(len(x)):
    if x[i]<smallest:
        smallest=x[i]
    if x[i]>largest:
        largest=x[i]   
print(smallest)  
print(largest)
