# guess a number from 1 to 10
from random import randint

# version 1 - 2 while loops are used
# play_again = None

# while play_again != "n":
#     guess = None
#     random_number = randint(1, 10)
#     while guess != random_number:
#         guess = int(input("Guess a number between 1 and 10: "))
#         if guess < random_number:
#             print("Too low, try again")
#         elif guess > random_number:
#             print("Too high, try again")
#     print("You guessed it! You won!")
#     play_again = input("Do you want to keep playing? (y/n) ")

# version 2 - 1 while loop used with a break statement
random_number = randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_number:
        print("Too low, try again")
    elif guess > random_number:
        print("Too high, try again")
    else:
        print("You guessed it! You won!")
        play_again = input("Do you want to keep playing? (y/n) ")
        if play_again == "y":
            random_number = randint(1, 10)
        else:
            break