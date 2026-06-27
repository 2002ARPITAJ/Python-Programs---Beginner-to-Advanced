Age = int(input("Please enter your age: "))
Citizen = input("Are you a citizen of India?? y/n ")

if Citizen == 'y':
    if Age>=18:
        print("Congratulations!!!! You are eligible for voting")
    elif Age<18:
        print("Sorry kiddo!!! We understand your enthuastism but come back when you are above 18!")
    else:
        print("Invalid Input")
else:
    print("Chal haat pardeshiii!!!!")