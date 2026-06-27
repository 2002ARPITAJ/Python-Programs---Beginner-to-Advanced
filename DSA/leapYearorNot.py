print("Leap day occurs once in every four years in the month of february")
year = int(input("Enter the year : "))


if (year % 400 == 0) or (year %100 != 0 and year % 4 == 0):
    print("Its a Leap year!!!!")
else:
    print("Its not a Leap year!!!!")