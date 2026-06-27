n = int(input("Enter the number of the elements in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)
print(numbers)

largest = float('-inf')
smallest = float('inf')

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)