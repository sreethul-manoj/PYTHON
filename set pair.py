numbers = [2, 4, 3, 7, 5, 8, 1,0]
target = 9


n = len(numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:  
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  


    left = 0
right = len(numbers) - 1
pairs = []

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:  
        pairs.append((numbers[left], numbers[right]))
        left += 1 
        right -= 1  
    elif current_sum < target:
        left += 1 
    else:
        right -= 1  

        
if pairs:
    for pair in pairs:
        print(pair)
else:
    print("No pairs found")

