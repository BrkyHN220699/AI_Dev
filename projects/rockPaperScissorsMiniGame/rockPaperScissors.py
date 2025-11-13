import random


computerChoices = ["rock", "paper", "scissors"]

computerChoice = random.choice(computerChoices)

inputUser = input("Enter rock, paper or scissors: ").lower()

print("Computer chose:", computerChoice, "and you chose:", inputUser)

if inputUser == computerChoice:
    print("It's a tie! Both chose", computerChoice, inputUser)

elif (inputUser == "rock" and computerChoice == "scissors"):
    print("You win! Rock crushes Scissors")

elif (inputUser == "rock" and computerChoice == "paper"):
    print("You lost! Paper covers Rock")

elif (inputUser == "paper" and computerChoice == "rock"):
    print("You win! Paper covers Rock")

elif (inputUser == "paper" and computerChoice == "scissors"):
    print("You lost! Scissors cut Paper")

elif (inputUser == "scissors" and computerChoice == "paper"):
    print("You win! Scissors cut Paper")

elif (inputUser == "scissors" and computerChoice == "rock"):
    print("You lost!  Rock crushes Scissors")


