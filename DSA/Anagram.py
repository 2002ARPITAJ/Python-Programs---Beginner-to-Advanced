word1 = input("Enter first string: ")
word2 = input("Enter second string: ")

if len(word1) != len(word2):
    print("Not Anagram")
else:
    freq = {}

    # Count characters of first string
    for ch in word1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Reduce frequency using second string
    for ch in word2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("Not Anagram")
            exit()

    # Check whether every frequency became 0
    anagram = True

    for value in freq.values():
        if value != 0:
            anagram = False
            break

    if anagram:
        print("Anagram")
    else:
        print("Not Anagram")

#My solution

word1 = input("Enter the string : ")
word2 = input("Enter the string: ")

freq = {}
freq1 = {}

for char in word1:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char in word2:
    if char in freq1:
        freq1[char] += 1
    else:
        freq1[char] = 1

# Direct comparison instead of a nested loop
if freq == freq1:
    print("The strings have identical character frequencies (Anagrams!).")
else:
    print("The strings do not match.")