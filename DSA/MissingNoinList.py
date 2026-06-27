numbers = [1, 2, 3, 4, 7, 8]

for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] > 1:
        print("Missing number:",numbers[i-1]-1)
        break
    
print("No Missing numbers")