import random
game_state = True
turns = 0

def random_numbers():
    num = random.randint(10000,99999)
    digits = [int(d) for d in str(num)]
    return digits

def evaluate_attempt(myNums, userNums, turns, game_state):
    turns += 1
    if myNums == userNums:
        game_state = False
        return f'answer is correct. It took you {turns} turns'
    else:
        heads = 0
        tails = 0
        for i in range(len(myNums)):
            num1 = myNums[i]
            num2 = userNums[i]
            if num1 == num2:
                heads += 1
            else:
                if num2 in myNums:
                    tails += 1
        return f"heads: {heads}, tails: {tails}"

# myNums = random_numbers()
myNums = [1,2,3,4,5]
def game_play(game_state, myNums):
    user_guess = input('put in a 5 digit number')
    while len(user_guess) != 5:
        user_guess = input('make sure you put 5 digit numbers')
    userNums = [int(d) for d in str(user_guess)]
    return evaluate_attempt(myNums, userNums, turns, game_state)


if __name__ == "__main__":
    while True:
        attempt = game_play(game_state, myNums)
        print(attempt)
        if game_state == False:
            break
