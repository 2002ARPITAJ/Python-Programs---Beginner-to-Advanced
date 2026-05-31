numbers = [10, 20, 30, 40, 50]
num = int(input("Enter the number to be searched: "))

for i in range(len(numbers)):
    if numbers[i] == num:
        print("Found")
        break
else:
    print("Not Found")





