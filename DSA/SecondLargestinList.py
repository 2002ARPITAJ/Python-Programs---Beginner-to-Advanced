numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)

# Method 2 without duplicates elements

numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)

# method 3 - asking user to enter the array elements

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Array:", numbers)
print("Largest:", largest)
print("Second Largest:", second_largest)

# edge case where array is 10,10 - there wont be any 

n = int(input("Enter the number of elements to be in array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter elements {i+1} : "))
    numbers.append(num)

print("Original Array:", numbers)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num  

print("Largest : ", largest)

# The fix to handle the edge case where no second largest exists
if second_largest == float('-inf'):
    print("Second_largest : -1")
else:
    print("Second_largest : ", second_largest)