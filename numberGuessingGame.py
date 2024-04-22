import random

def number_guessing_game(low, high, attempts):
    # Generate a random number between low and high
    number = random.randint(low, high)
    print(f"Guess the number between {low} and {high}. You have {attempts} attempts.")

    # Initialize the number of guesses
    guesses = 0

    # Game loop
    while guesses < attempts:
        # Ask the user for a guess
        guess = input("Enter your guess: ")
        
        # Try to convert the guess to an integer, handle invalid input
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        # Increment the number of guesses
        guesses += 1

        # Check if the guess is correct
        if guess == number:
            print(f"Congratulations! You guessed the number in {guesses} attempts.")
            break
        # Give hints to the player
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        
        # Check if the player has run out of attempts
        if guesses == attempts:
            print(f"Sorry, you've run out of attempts. The number was {number}.")

# Set the range and number of attempts
low = 1
high = 100
attempts = 10

# Start the game
number_guessing_game(low, high, attempts)
