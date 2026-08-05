import random

words = ["apple", "mango", "grapes", "banana", "orange"]
word = random.choice(words)

guessed = []
chances = 6

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        chances -= 1
        print("Wrong Guess! Chances left:", chances)

if chances == 0:
    print("You Lost! Word was:", word)