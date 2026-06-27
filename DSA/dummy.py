numbers = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] > 1:
        count+=1
        print("Missing number:", numbers[i-1] + 1)
        break
if count == 0:
    print("No Missing numbers")
