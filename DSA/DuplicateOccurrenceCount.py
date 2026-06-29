numbers = [10, 20, 50, 60, 40, 10, 80, 60, 47, 47, 80]
num = int(input("Enter the number to be checked for duplicate: "))
n = 0

if num in numbers:
    for i in numbers:
        if i == num:
            n += 1

    if n > 1:
        print(f"{num} appears {n} times")
    else:
        print(f"{num} appears only once")
else:
    print("Entered number is not in the list")


# Method 2 - using Built in function
# numbers = [10, 20, 50, 60, 40, 10, 80, 60, 47]
# num = int(input("Enter the number to be checked for duplicate: "))

# count = numbers.count(num)

# if count > 1:
#     print(f"{num} appears {count} times")
# else:
#     print("No duplicate occurrences")

# Method 3

n = int(input("Enter the number of elements to be present in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print(numbers)

num = int(input("Enter the number to be checked : "))

if num in numbers:
    count = 0

    for i in numbers:
        if i == num:
            count += 1

    if count > 1:
        print(f"{num} appears {count} times")
    else:
        print(f"{num} appears only once")
else:
    print("Entered number is not in the list")

