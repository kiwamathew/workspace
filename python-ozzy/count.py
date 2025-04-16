# A program that counts the vowels in a string

word = input("Enter your preferred word: ")
vowels_in_word = []
for i in word:
    if i == "a":
        vowels_in_word.append(i)
    elif i == "e":
        vowels_in_word.append(i)
    elif i == "i":
        vowels_in_word.append(i)
    elif i == "o":
        vowels_in_word.append(i)
    elif i == "u":
        vowels_in_word.append(i)

print(vowels_in_word)

number_of_vowels = len(vowels_in_word)
print(number_of_vowels)
        
