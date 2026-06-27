n = int(input("Enter the number of elements in the array: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("Original Array:", numbers)

target = int(input("Enter the target : "))

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left+right) // 2
    if numbers[mid] == target:
        print("Found at Index: ", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1