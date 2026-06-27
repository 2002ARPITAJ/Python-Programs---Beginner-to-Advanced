print("A prime number is greater than 1 and divisible only by 1 and itself.")
number = int(input("Enter the number: "))

if number >= 1:
    for i in range(2, number):
        if number % i == 0:
            print("Its not a prime number")
            break
    else:
        print("Its a prime number")
else:
    print("Its not a prime number")


