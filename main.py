import random
from words import words

def get_word(words):
    word = random.choice(words)           # randomly chooses from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_word(words)
    world_letters = set(word)              # letters in the word#
    used_letters = set()                   # what the user has guessed#

    user_letter = input("Guess a letter: ")   # getting user input
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in world_letters:
            world_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("Character already been used. Try agian!")
    else:
        print("Invaild character. Please try agian!")

user_input = input("Type something: ")
print(user_input)
