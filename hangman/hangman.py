'''
Main script to play hangman. 
'''

import random


class Hangman:
    '''
    Class to play Hangman.
    The user is asked for letters, which are checked against a word. User wins if they guess each letter in the word before their lives run out.
    The word list and number of lives are defined in the main body.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    word_list: list
        The given word list
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(letter)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives):
        self.word = list(random.choice(word_list))
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        Checks if the guessed letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        Returns:
        --------
        True if guess in in word, else False
        '''
        in_word = guess in self.word
        self.list_of_guesses.append(guess)
        if in_word:
            for il, letter in enumerate(self.word):
                if letter==guess:
                    self.word_guessed[il] = guess

            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print("Sorry, %s is not in the word." % (guess))
            print("You have %s lives left." % (self.num_lives))
        
        print("Guessed so far: %s" % (self.word_guessed))
        
        
    def ask_for_input(self):
        '''
        Asks the user for a guessed letter and checks if:
        - the guess has already been tried
        - the character is a single character
        - the character is in the alphabet
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess = input("Choose a letter from the alphabet.").lower()
            if not (guess.isalpha() and len(guess)==1): # checks if guess is both in the alphabet and a single character
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: # checks if guess has already been tried
                print("You already tried that letter!")
            else: # valid guess, so run check_guess method
                self.check_guess(guess) 
                break

def play_game(word_list, num_lives=5):
    '''
    Defines an instance of the Hangman game.
    Iterates through the game and applies conditions for ending the game.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    '''
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
    print("The word was '%s'" % (''.join(str(x) for x in game.word)))           


if __name__ == '__main__':
    num_lives = 5
    word_list = ['mango', 'pear', 'apple', 'orange', 'banana']
    play_game(word_list, num_lives)



    

    

    
    


