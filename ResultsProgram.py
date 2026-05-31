marks = int(input("Enter your marks: "));

if marks >=90 and marks<=100:
    print("Congrats!!!! you have secured Distinction grade")
elif marks <=89 and marks>=80:
    print("First class")
elif marks <=79 and marks>=69:
    print("Second class")
elif marks <=68 and marks>=36:
    print("Third class")
else:
    print("Not at all sorry, you are failed")