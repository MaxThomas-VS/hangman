'''
milestone 5 for hangman project.
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
        # print(self.word) # for testing

    def check_guess(self, guess):
        if guess in self.word:
            return True
        else:
            return False
        

    def ask_for_input(self):
        while True:
            guess = input("Choose a letter from the alphabet.").lower()
            if not guess.isalpha() and len(guess)==1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                in_word = self.check_guess(guess)
                self.list_of_guesses.append(guess)
                if in_word:
                    for ix in range(len(self.word)):
                        if self.word[ix]==guess:
                            self.word_guessed[ix] = guess

                    print(self.word_guessed)
                    self.num_letters -= 1
                else:
                    self.num_lives -= 1
                    print("Sorry, %s is not in the word." % (guess))
                    print("You have %s lives left." % (self.num_lives))
                
                print("Guessed so far: %s" % (self.word_guessed))

                break


def play_game(word_list, num_lives=5):
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
    word_list = ['mango', 'pear', 'apple', 'orange', 'banana']
    play_game(word_list)



    

    

    
    


