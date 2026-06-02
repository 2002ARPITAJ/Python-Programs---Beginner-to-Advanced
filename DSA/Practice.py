numbers = [10, 20, 30, 40, 20, 10]

list = []

for num in numbers:
    duplicate = False

    for u in list:
        if u == num:
            duplicate = True
            break
    if not duplicate:
        list.append(num)

print("Original list:",numbers)
print("List without duplicates:", list)