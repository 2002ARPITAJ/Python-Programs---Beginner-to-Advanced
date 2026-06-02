numbers = [10, 80, 30, 40]

sorted = True

for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        sorted = False
        break

if sorted == True:
    print("Sorted")
else:
    print("Not Sorted")
