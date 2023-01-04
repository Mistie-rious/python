import random

top_number = input("Please type a number: ")

if top_number.isdigit():
    top_number = int(top_number)
    if top_number <= 0:
        print("Please type a number greater than zero! ")
        quit()

else: 
    print("Please type a real number!")
    quit()

guesses = 0

random_number = random.randint(0, top_number)

while True:
    guesses += 1
    guess = input("Make a guess:")
    if guess.isdigit():
        guess = int(guess)

    else: 
        print("Please type a real number!")
        quit()

    if random_number == guess:
        print('Congrats! You gussed the number!')
        break
    elif guess > random_number:
        print("Your guess is higher than the number!")
    else:
        print("Your guess is lower than the number!")


print("You got it in", guesses, "guesses!")