import random
Random_number = (random.randrange(1,10))

secret_number = Random_number
guess_count = 0
guess_limit = 10

while guess_count < guess_limit:
    guess = int(input("Guess a number 1-10: "))
    print(Random_number)
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        print(f"The number was {Random_number}")

        break
else:
    print("You Failed!")
    print(f"The number was {Random_number}")