numbers = [10, 20, 30, 40, 20, 10]

printed = []

for num in numbers:

    if num not in printed:

        count = 0

        for n in numbers:
            if n == num:
                count += 1

        print(f"{num} occurs {count} times")
        printed.append(num)