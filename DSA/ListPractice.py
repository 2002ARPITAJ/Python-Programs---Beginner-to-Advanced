numbers = [10, 20, 30, 40, 50]
print(numbers)

data = [45, "Arpita", 9.9, True]
print(data)

# Method 1
print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])

# Method 2
for num in numbers:
    print(num)

# Method 3
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# Method 4
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-0])

# Method 5
print(data[0])

# Method 6
numbers.append(60)
print(numbers)
print(len(numbers))
numbers.remove(60)
print(numbers)

# Method 7
print(len(numbers))