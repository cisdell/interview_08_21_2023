import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = self.generate_target_number()
        self.num_guesses = 0

    def generate_target_number(self):
        return str(random.randint(10000, 99999))

    def evaluate_guess(self, guess):
        self.num_guesses += 1
        heads = 0
        tails = 0

        for i in range(len(self.target_number)):
            if guess[i] == self.target_number[i]:
                heads += 1
            elif guess[i] in self.target_number:
                tails += 1

        return heads, tails

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
