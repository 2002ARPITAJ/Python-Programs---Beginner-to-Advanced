tableNum = int(input("Enter the number : "))

start = 1

if tableNum > 1:
    for i in range(1,11):
        result = tableNum * i
        print(f"{tableNum} * {i} = {result}")
else:
    print("Invalid Number")