#  Method 1
numbers = [10, 40, 67, 99, 34, 59, 97, 1]

even = 0
odd = 0

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        even += 1
    elif numbers[i] % 2 == 1:
        odd += 1
print("Total even numbers in the list is :", even)
print("Total off numbers in the list is : ", odd)

# Method 2

numbers = [10, 40, 67, 99, 34, 59, 97, 1]

even = 0
odd = 0

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers count :", even)
print("Odd numbers count : ", odd)