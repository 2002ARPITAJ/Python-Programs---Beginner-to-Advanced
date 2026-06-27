n = int(input("Enter the number of elements to be present in the array : "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)

print("Original array:", numbers)

left = 0
right = len(numbers) - 1

is_palindrome = True

while left < right:

    if numbers[left] != numbers[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")