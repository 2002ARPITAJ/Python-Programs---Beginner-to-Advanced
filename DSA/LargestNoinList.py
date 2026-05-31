numbers = [10, 40, 80, 90, 66, 1000, 777, 555, 6789]

largest = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

print("Largest number: ", largest)


