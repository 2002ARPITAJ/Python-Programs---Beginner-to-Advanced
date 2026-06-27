n = int(input("Enter the number of the array elements : "))

numbers = []
count = 0

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)
print(numbers)


seen = []

for num in numbers:
    if num in seen:
        print("First repeating element:", num)
        break

    seen.append(num)