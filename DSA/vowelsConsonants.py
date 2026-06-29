# Use a clear name for the full string
user_string = input("Enter the string: ")

vowels = 0
consonants = 0

# Iterate directly through each character in the string
for char in user_string:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():  # Ensures we only count actual letters as consonants
        consonants += 1

print("Vowels : ", vowels)
print("Consonants: ", consonants)