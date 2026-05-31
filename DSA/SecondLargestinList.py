numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

largest = numbers[0]

for i in range(1,len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]

print("Largest number :", largest)
numbers.remove(largest)
Slargest = numbers[0]
for i in range(1,len(numbers)):
    if numbers[i] > Slargest:
        Slargest = numbers[i]

print("Second largest number : ", Slargest)
numbers.append(largest)


# Method 2
numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

largest = numbers[0]
second_largest = numbers[0]

for i in range(1, len(numbers)):

    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]

    elif numbers[i] > second_largest:
        second_largest = numbers[i]

print("Largest:", largest)
print("Second largest:", second_largest)