from tkinter.messagebox import YES


print("Welcome to Mistie's quiz!")

playing = input("Would you like to play? ")
if playing.lower() != "yes":
    quit()
score = 0

answer = input("What is Mistie's favorite colour? ")
if answer.lower() == "purple":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Mistie's favorite food? ")
if answer.lower() == "spaghetti":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Mistie's favorite number? ")
if answer == "7" or "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Mistie's favorite anime? ")
if answer.lower() == "fruits basket":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is Mistie's favorite artist? ")
if answer.lower() == "frank ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Mistie's favorite anime genre? ")
if answer.lower() == "romance":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

cont = input("Congrats you're done with the quiz! Would you like to know what you got?")
if cont.lower() != "yes":
    quit()
if score >= 6:
    print("You got all questions correct!yYou really know her huh?")
else:
    print("You got " + str(score) + " questions correct!")

