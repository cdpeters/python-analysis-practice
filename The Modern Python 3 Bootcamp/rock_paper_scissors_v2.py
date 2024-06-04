# rock-paper-scissors with 1 human player and 1 computer player ("AI")
from random import randint

player_wins = 0
computer_wins = 0
required_wins = 2
flag = False

print("Welcome to rock-paper-scissors")

while player_wins < required_wins and computer_wins < required_wins:
    print()
    print(f"Player Score: {player_wins}, Computer Score: {computer_wins}")
    player = input("Enter either rock, paper or scissors: ").lower()
    # add a quit option
    if player == "quit" or player == "q":
        flag = True
        break
    num = randint(0,2)
    if num == 0:
        computer = "rock"
    elif num == 1:
        computer = "scissors"
    else:
        computer = "paper"

    print(f"Computer plays: {computer}")

    if player == computer:
        print("It is a draw!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move.")
if not flag:
    print(f"FINAL SCORE... Player Score: {player_wins}, Computer Score: " +
          f"{computer_wins}")
    if player_wins > computer_wins:
        print(f"Congratulations, you won the best of {2*required_wins - 1}!")
    else:
        print(f"Too bad, the computer won the best of {2*required_wins - 1}.")