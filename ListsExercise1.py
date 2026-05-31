numbers = [10, 20, 30, 40, 50]


print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length:", len(numbers))
for i in range(len(numbers)):
    print(numbers[i])

print("Second element:", numbers[0+1])
sum = numbers[0+1] + numbers[0+2]
print("Sum of the second element and third element:", sum)

n = int(len(numbers))

for i in range(1, n+1):
    print(numbers[-i])