'''
milestone 2 for hangman project
'''

import random

if __name__ == '__main__':
    word_list = ['mango', 'pear', 'apple', 'orange', 'banana']
    print(word_list)
    word = random.choice(word_list)
    print(word)
    guess = input("Choose a letter from the alphabet.")
    if guess.isalpha() and len(guess)==1:
        print("Good guess!")
    else:
        print("Oops! That's not a vaid input.")

    
    