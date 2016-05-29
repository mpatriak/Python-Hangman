#!/usr/bin/env python 2

from random import *

player_score = 0
computer_score = 0

# Define the graphics that will be used in the game
def hangedman(hangman):
    graphic = [
        """
            +-------+
            |
            |
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            | 
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |       |
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      /
            |
         ==============
        """
            ,
        """
            +-------+
            |       |
            |       0
            |      -|-
            |      / \
            |
         ==============
        """]
    print(graphic[hangman])

def start():
    print ("Let's play a game of Linux Hangman")
    while game():
        # pass will exit the loop if the player is done
        pass
    scores()

def game():
    # Create a set of words to play the game with
    dictionary = ["cat", "dog", "bird", "nest", "sun", "tree"]
    # Use the choice function from random mod to select a word
    word = choice(dictionary)
    word_length = len(word)
    # Create a clue with the number of underscores
    # equal to the word's length
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    # Set up a loop that continues until player wins or loses
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        # Make sure entry is numeric and only 1 character long
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print ("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                # Search the word for the entered letter
                first_index = word.find(letter)
                # If letter is correct, let user know
                if first_index == -1:
                    letters_wrong += 1
                    print ("Sorry,",letter,"isn't what we're looking for.")
                else:
                    print ("Congratulations, ",letter," is correct.")
                    # Loop through the word and change the specific letter
                    # that is correct
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print ("Choose another.")

        # Display the graphic
        hangedman(letters_wrong)
        # Print what the clue currently looks like
        print (" ".join(clue))
        print ("Guesses: ", letters_tried)

        # Check if the game is over
        if letters_wrong == tries:
            print ("Game Over")
            print ("The word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print ("You win!")
            print ("The word was", word)
            player_score += 1
            break
    return play_again()

# Get user input, sanitize, display it, and return it to be used
def guess_letter():
    letter = input("Take a guess at our mystery word: ")
    letter.strip()
    letter.lower()
    print (letter)
    return letter

# Ask to play again
def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print ("Thank you very much for playing!")

def scores():
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("Player: ", player_score)
    print ("Computer: ", computer_score)

# Used to execute in command line or import
# into another Python script. This will prevent
# the code from being executed when being imported.
if __name__ == '__main__':
    start()
