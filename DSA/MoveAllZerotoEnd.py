n = int(input("Enter the number of elements in the array : "))

numbers = []
number = []
number2 = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)
print("Before moving zeroes to end : ",numbers)

for num in numbers:
    if num == 0:
        number.append(num)
    else:
        number2.append(num)

merged = number2 + number
print("After moving all zeroes : ", merged)
        

