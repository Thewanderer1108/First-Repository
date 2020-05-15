# this is a program for a rock, paper, scissors game.
p1 = input("Player 1. Your Name: ")
p2 = input("Player 2. Your Name: ")
ch1 = input("Player 1 - {} what do you choose from Rock, Paper and Scissors? ".format(p1))
ch2 = input("Player 2 - {} what do you choose from Rock, Paper and Scissors? ".format(p2))
if ch1 == ch2:
    print("Its a tie!!")
elif ch1 == "rock":
    if ch2 == "scissors":
        print("{} Wins!!".format(p1))
    else:
        print("{} Wins!!".format(p2))
elif ch1 == "scissors":
    if ch2 == "paper":
        print("{} Wins!!".format(p1))
    else:
        print("{} Wins!!".format(p2))
elif ch1 == "paper":
    if ch2 == "rock":
        print("{}, Wins!!".format(p1))
    else:
        print("{}, Wins!!".format(p2))
else:
    print("Please enter a valid choice.")



