# Problem 1
"""
import random

num_of_guesses = 0

print("What's your name?")
name = input()

answer = random.randint(1, 50)
print("Hey", name, ", I'm thinking of a number between 1 and 50.")

while num_of_guesses < 7:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    num_of_guesses += 1
    if guess < answer:
        print("Number is too low!")
    if guess > answer:
        print("Number is too high!")
    if guess == answer:
        break
if guess == answer:
    num_of_guesses = str(num_of_guesses)
    print("Well done", name, ", you guessed the number in: ", num_of_guesses)

if guess != answer:
    num_of_guesses = str(answer)
    print("Wrong! Unlucky, the number was: ", answer)

"""
# Problem 2

import random

answer = random.randint(1, 50)
count = 1
guess = None
play = True

while guess != answer:
    guess = input("I'm thinking of a number between 1- and 50. Try and guess: ")
    if guess.isdigit():
        guess = int(guess)
        play = False
    if guess < answer:
        print("Number is too low!")
    if guess > answer:
        print("Number is too high!")
    if guess == str(""):
        print("Doh!")
