n = int(input("Enter the number of the elements in the array "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1} : "))
    numbers.append(num)
print(numbers)

first = numbers[0]

for i in range(len(numbers)-1):
    numbers[i] = numbers[i+1]

numbers[-1] = first

print(numbers)



# method 2 

# first = numbers[0]

# for i in range(len(numbers)-1):
#     numbers[i] = numbers[i+1]

# numbers[-1] = first

# print(numbers)
