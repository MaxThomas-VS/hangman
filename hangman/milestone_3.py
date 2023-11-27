'''
milestone 3 for hangman project
'''
import random

if __name__ == '__main__':
    word_list = ['mango', 'pear', 'apple', 'orange', 'banana']
    print(word_list)
    word = random.choice(word_list)
    print(word)

    while True:
        guess = input("Choose a letter from the alphabet.")
        if guess.isalpha() and len(guess)==1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    if guess in word:
        print("Good guess! %s is in the word." % (guess))
    else:
        print("Sorry, %s is not in the word. Try again." % (guess))

    
    


