import random

choices = ["rock", "paper", "scissor"]

while True:
    try:
        userinput = input("Select Rock, Paper, or Scissor (or 'q' to quit): ").lower()

        if userinput == "quit" or userinput == "q":
            print("Goodbye!")
            break
        if userinput not in choices:
            raise ValueError(f"'{userinput}' is not a valid choice.")
    except ValueError:
        print("Invalid input. Please choose rock, paper, or scissor.")
        continue

    computerchoice = random.choice(choices)
    print(f"Computer chose: {computerchoice}")

    if userinput == computerchoice:
        print("It's a tie! Try again.")
    elif (userinput == "rock" and computerchoice == "scissor") or \
         (userinput == "paper" and computerchoice == "rock") or \
         (userinput == "scissor" and computerchoice == "paper"):
        print("You win!")
        break
    else:
        print("You lose. Try again.")