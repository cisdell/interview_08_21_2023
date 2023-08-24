from game_logic import NumberGuessingGame

if __name__ == "__main__":
    game = NumberGuessingGame()
    print("Welcome to the Game!")

    while True:
        user_guess = input("Enter a number: ")
        if len(user_guess) != 5 or not user_guess.isdigit():
            print("Please enter a valid 5-digit number.")
            continue

        heads, tails = game.evaluate_guess(user_guess)
        print(f"{heads} heads, {tails} tails")

        if user_guess == game.target_number:
            print(f"Congratulations! You guessed the number in {game.num_guesses} guesses.")
            break
