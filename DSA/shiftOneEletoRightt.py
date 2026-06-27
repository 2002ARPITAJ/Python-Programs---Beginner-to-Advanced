n = int(input("Enter the number of elements in the array: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("Original Array:", numbers)

last = numbers[-1]

for i in range(len(numbers)-1, 0, -1):
    numbers[i] = numbers[i-1]

numbers[0] = last

print("Array after right rotation:", numbers)