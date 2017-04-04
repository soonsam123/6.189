# Name: Soon Sam R Santos
# Section: Project Hangman
# 6.189 Project 1: Hangman template
# hangman.py
from random import randrange
from string import *      #To use the string modules. join() and lower()
# secret_world: Word the user is trying to guess. (string)
# letters_guessed: Letters he already guessed. (list)
# mistakes_made: The number of incorrect letters. (int)

#Helper Code ------------- You don't need to understand.
#Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------

#secret_world : "claptrap"
# MAX_GUESSES = 6 upper case letter --> numbers I don't plan to change.

#CONSTANTS
#MAX_GUESSES = 6
#GLOBAL VARIABLES
#secret_word = 'claptrap'
letters_guessed = []

#See if the user guess was right or wrong.
def word_guessed(letters_guessed):
    count = 0
    for letter in secret_word:
        if letter in letters_guessed:
            count = count + 1
    if count == len(secret_word):
        return True
    else:
        return False

#Print what the user already know.
def print_guessed(letters_guessed):
    current_word = ['_','_','_','_','_','_','_','_',]
    i = 0
    while i < len(secret_word):
        if secret_word[i] in lower(join(letters_guessed,'')):  #Turning into a string and putting in lowercase. To make possible uppercase guesses.
            current_word[i] = secret_word[i]     #'_' in current word will be substituted by some letter, if there is.
        i=i+1
    return join(current_word,'')   #Outputing not the list, but the string.

def play_hangman(list):
    secret_word = get_word()
    i = 0
    MAX_GUESSES = 6
    print  "You have %s guesses left" %(MAX_GUESSES)  #You have 6 guesses left. In the first time
    while i < len(list) :   #Going through the letters the user guessed. List of letters.  List of length 7. i goes from 0 to 6
        
        if list[i] not in list[:i]:                                  #If the letter was not cited in the previous letters.
            print print_guessed(list[:i+1])                          #Print how far the user knows the word. i+1 to begin with [0:1] and finish with [0:7] with list of length 7.
                                                                     #this make print_guessed be tested for all the slice of letters in the list.
            MAX_GUESSES = MAX_GUESSES - 1                            
                     
            print  "You have %s guesses left" %(MAX_GUESSES)

            if (word_guessed(list[:i+1])==True):
                return "YOU WON THE GAME"  #If the list so far has already found the word. The user won the game.
            if (MAX_GUESSES == 0):
                return "GAME IS OVER"              #If the chances are over. Game is Over.            
            
        else:  #In case the letter is in the previous list, the user already typed this letter. No guesses. 
            print "You already guessed this letter"
            print "You have %s guesses left" %(MAX_GUESSES)
        i = i + 1
print play_hangman(['j','j','j','j','j','j','j','j']) #Should return You already guessed this letter.
print "-----------------------------"
print play_hangman(['j','k','g','i','k','o','u','z']) #Should return GAME IS OVER
print "-----------------------------"
print play_hangman(['a','m','p','l','t','r','c']) #Should return GAME IS OVER BEFORE I GET RIGHT.    
print "-----------------------------"
print play_hangman(['a','p','l','t','r','c']) #Should Win in the last chance
