import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()        # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a', 'b', 'c']) -> 'a b c'
        print(f"You have {lives} lives left and you have \
already used the letters: ", " ".join(used_letters))

        # what the current word is with spaces (w _ o r d)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word is: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in word.")
        
        elif user_letter in used_letters:
            print("You have already used this letter. Please try again")
        
        else:
            print("Please type in a valid letter.")
    
    if lives == 0:
        print (f"You lost. the word was {word}")
    else:
        print(f"You guessed the word {word} !!")

hangman()