'''
milestone 4 for hangman project.
'''
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = list(random.choice(word_list))
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in word:
            print("Good guess! %s is in the word." % (guess))
        else:
            print("Sorry, %s is not in the word. Try again." % (guess))

    def ask_for_input(self):
        while True:
            guess = input("Choose a letter from the alphabet.").lower()
            if not guess.isalpha() and len(guess)==1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



            

if __name__ == '__main__':
    word_list = ['mango', 'pear', 'apple', 'orange', 'banana']
    print(word_list)
    word = random.choice(word_list)
    print(word)


    game = Hangman(word_list)
    game.ask_for_input()



    

    

    
    


