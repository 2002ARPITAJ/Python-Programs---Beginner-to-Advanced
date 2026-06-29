word1 = input("Enter first string : ")
word2 = input("Enter second string : ")

if len(word1) != len(word2):
    print("Anagram")
else:
    freq = {}

    for ch in word1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        
    for ch in word2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("Not Anagram")
            exit()

    anagram = False

    for value in freq.values():
        if value != 0:
            anagram = False
            break

    if anagram:
        print("Anagram")
    else:
        print("Not a Anagram")