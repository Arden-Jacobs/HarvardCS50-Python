import random

while True:
    try:
        lev = int(input("Level: "))
        if lev > 0:
            break
    except ValueError:
        lev = input("Level: ")

num = random.randint(0, lev)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            guess = int(input("Guess: "))
        if guess == num:
            print("Just right!")
            break
        if guess > num:
            print("Too large!")
        if guess < num:
            print("Too small!")
    except ValueError:
        pass

print(num)