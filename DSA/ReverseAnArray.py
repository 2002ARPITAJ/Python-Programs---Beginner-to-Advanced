n = int(input("Enter the number of elements to be present in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)

print(numbers)

number = []

for i in range(len(numbers)-1,-1,-1):
    number.append(numbers[i])

print("Reversed array : ", number)


#Method 2 : Using pointers reducing the space complexity

n = int(input("Enter the number of elements to be present in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)

print("Original array:", numbers)

# --- IN-PLACE REVERSAL START ---

# Initialize your two pointers
left = 0
right = len(numbers) - 1

# Loop until the pointers meet in the middle
while left < right:
    # Pythonic swap: swaps the values at left and right indices instantly
    numbers[left], numbers[right] = numbers[right], numbers[left]
    
    # Move the pointers closer together
    left += 1
    right -= 1

# --- IN-PLACE REVERSAL END ---

print("Reversed array : ", numbers)