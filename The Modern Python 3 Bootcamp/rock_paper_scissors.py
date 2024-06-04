# rock-paper-scissors with 2 human players
print("Welcome to rock-paper-scissors")

player1 = str(input("Player 1, enter either rock, paper or scissors: "))
player2 = str(input("Player 2, enter either rock, paper or scissors: "))

print ("SHOOT!")

if player1 == player2:
    print("It is a draw!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "rock":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
else:
    print("Something went wrong, try again.")

# here is a shorter way where draw conditions are checked first, then only
# player1 win conditions are checked followed by an else "player2 win". Note,
# there is no error handling in this version
# if player1 == player2:
#     print("It is a draw!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("Player 1 wins!")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("Player 1 wins!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("Player 1 wins!")
# else:
#     print("Player 2 wins!")