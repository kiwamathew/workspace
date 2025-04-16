# A program that counts the vowels in a string

word = input("Enter your preferred word: ")
vowels_in_word = []
for i in word:
    if i == "a" or "e" or "i" or "o" or "u":
        vowels_in_word.append(i)
    print(vowels_in_word)
        
