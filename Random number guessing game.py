import random
import math


print("Welcome to the Number Guessing Game!")
    
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))
    
random = random.randint(lower, upper)   

minguesses = math.ceil(math.log2(upper - lower + 1))
print("You have to guess the number in a minimum of " +str(minguesses)+ " guesses.")
    
guess_count = 0
    
while True:
    user_guess = int(input("Enter your guess: "))
    guess_count += 1
        
    if user_guess > random:
        print("Try Again! You guessed too high.")
    elif user_guess < random:
        print("Try Again! You guessed too small.")
    else:
        print(f"Congratulations! You've guessed the number in " + str(guess_count) + " guesses.")
        break
        
    if guess_count > minguesses:
        print("Better Luck Next Time!")
        break
