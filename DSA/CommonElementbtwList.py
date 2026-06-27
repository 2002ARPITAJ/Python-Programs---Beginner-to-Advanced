list1 = [10, 20, 30, 40]
list2 = [30, 40, 40, 50, 60]

list3 = []
for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            list3.append(num1)
            break   # stop checking once found

print("Original list1:", list1)
print("Original list2:", list2)
print("Numbers common among lists:", list3)
