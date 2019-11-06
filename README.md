# sofreshsoclean
# Problem 1 # Completed
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
    
    # Problem 2 has to be modified to let the user know that they can only use integers
