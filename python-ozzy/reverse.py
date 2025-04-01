# A program that reverses a string.
'''name  = "Mathew Kiwanuka"
reversed_name = name[::-1]
print(reversed_name)'''

def reverse_string(*args):
    word = args
    word = str(input("Please enter your word: "))
    reversed_word = word[::-1]
    
    print(reversed_word)


reverse_string()