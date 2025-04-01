# Program that generates a random number and asks you to input what you think the number is.
import random
random_number = random.randint(1,10)
user_number = int(input("Please enter a number between 1 and 10 that you are thinking of: "))
if user_number == random_number:
    print(f"Congratulations! You guessed right. That is the same number as the computer generated which is {random_number}")
else:
    print(f"Oops! Unfortunately, the number you guessed is {user_number} and the computer generated {random_number}")