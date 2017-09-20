import random

highest = 10
answer = random.randint(1, highest)

guess = 0

guess = int(input("Please guess a number between 1 and {}: ".format(highest)))

while guess != answer:
    if guess == 0:
        break
    elif int(guess) > answer:
        guess = int(input("Please guess a lower number: ".format(highest)))
    elif int(guess) < answer:
        guess = int(input("Please guess a higher number: ".format(highest)))
    else:
        guess = int(input("Please guess a number between 1 and {}: ".format(highest)))

if int(guess) == answer:
    print("You guessed it! The answer was {}".format(answer))
