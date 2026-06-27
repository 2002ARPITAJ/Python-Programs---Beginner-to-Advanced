# with duplicate elements
numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)


#without duplicate elements

numbers = [10, 90, 70, 65, 45, 78, 93, 23, 34]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:

    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest:
        second_smallest = num

print("Smallest:", smallest)
print("Second Smallest:", second_smallest)

# edge case where array is 10,10 - there's no second smallest

n = int(input("Enter the number of elements to be entered in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)

print("Original Array:", numbers)

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    # FIXED: Changed 'num < smallest' to 'num < second_smallest'
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest : ", smallest)

if second_smallest == float('inf'):
    print("There's no second smallest number")
else:
    print("Second smallest : ", second_smallest)