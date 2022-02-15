import random 
from termcolor import colored

def print_menu():
    print("Welcome to Lingordle!")
    print("Type a 5 letter word and hit enter!")

def pick_word():
    with open("lingordle.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)
    
print_menu()

word = pick_word()

for attempt in range(6):
    guess = input().lower()

    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(colored(guess[i], 'green'), end = "")
        elif guess[i] in word:
            print(colored(guess[i], 'yellow'), end = "")
        else:
            print(guess[i], end = "")
    print()
    
    if guess == word:
        print(f"Congrats! You got the lingordle in {attempt} tries.")
        #print(f"Press C-c to quit.")
        exit()
    elif attempt == 5:
        print(f"The lingordle was {word}.")
        #print(f"Press C-c to quit.")
