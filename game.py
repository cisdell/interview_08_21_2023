import random

game_state = True
turns = 0

def random_numbers():
    num = random.randint(10000,99999)
    digits = [int(d) for d in str(num)]
    return digits

test = random_numbers()

# print(test)

def game_play(game_state):
    user_guess = input('put in a 5 digit number')
    while len(user_guess) != 5:
        user_guess = input('make sure you put 5 digit numbers')





game_play(game_state)