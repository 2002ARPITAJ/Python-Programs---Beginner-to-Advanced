numbers = [10, 20, 30, 40, 20, 10]

unique_list = []

for num in numbers:
    duplicate_status = False

    for u in unique_list:
        if u == num:
            duplicate_status = True
            break
    if not duplicate_status:
        unique_list.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_list)