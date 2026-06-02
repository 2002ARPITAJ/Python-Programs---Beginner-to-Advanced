numbers = [10, 50, 60, 44, 82, 77]

Avg = 0
total = 0
for i in range(0, len(numbers)):
    total = total + numbers[i]

Avg = total/len(numbers)
print("Average of the list numbers:", Avg)
