numbers = [20, 60, 44, 77, 99, 11, 3]

smallest = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < smallest:
        smallest = numbers[i]
print("Smallest number is : ", smallest)