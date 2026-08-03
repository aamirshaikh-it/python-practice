import random

while True:
    random_number = random.randint(1, 100)
    attempt = 0

    while True:
        try:
            guessing_number = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempt += 1

        if guessing_number < random_number:
            print("Too low! Try again.")
        elif guessing_number > random_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed it.")
            break

        print(f"Attempts so far: {attempt}")

    print(f"You guessed it in {attempt} attempts!")

    while True:
        response = input("Do you want to play again? (yes/no): ").lower().strip()

        if response == "yes" or response == "y":
            play_again = True
            break
        elif response == "no" or response == "n":
            play_again = False
            break
        else:
            print("Please type yes or no.")

    if not play_again:
        print("Thanks for playing! Goodbye.")
        break