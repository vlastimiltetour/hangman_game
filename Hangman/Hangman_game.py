import random
import string

from hangman_words import words

def get_clean_word():
    clean_word = random.choice(words)
    while '-' in clean_word or ' ' in clean_word:
        clean_word = random.choice(words)

    return clean_word


def play_hangman():
    lives = 3
    secret_word = get_clean_word().upper()
    guessed_secret_word_letters = set(secret_word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    print('Welcome to the hangman game!')
    print(secret_word)

    while lives > 0 and len(guessed_secret_word_letters) > 0:

        current_word = [letter if letter in used_letters else '-' for letter in secret_word]
        print('The current word:', ' '.join(current_word))
        user_letters = input('Type a letter: ').upper()

        #match
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in guessed_secret_word_letters:
                guessed_secret_word_letters.remove(user_letters)
            else:
                print('Wrong guess. Fail. You are losing a life.')
                lives = lives - 1
                print(f'You have {lives} lives.\n')

        #same letter
        elif user_letters in used_letters:
            print('You have used this letter. Guess again')
        else:
            print('This is not a letter!')


    if lives == 0:
        print('You have died! Game over.')
    else:
        print('Good! You won!')

play_hangman()