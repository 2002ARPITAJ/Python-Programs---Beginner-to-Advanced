n = int(input("Enter the number of elements to be present in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)

print("Original array:", numbers)


# Step 1: Build the frequency dictionary
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Step 2: Scan the original array to find the first unique element
found_unique = False
for num in numbers:
    if counts[num] == 1:
        print("First unique element:", num)
        found_unique = True
        break

if not found_unique:
    print("No unique elements found.")

