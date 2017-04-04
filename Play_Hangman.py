# Name: Soon Sam R Santos
# Section: Lecture 6
# 6.189 Project 1: Hangman template
# hangman_template.py

# CREDITS ---> Art created by sk
# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *  #This take the functions in hangman _lib. So I can use it righ here without having the functions in this prompt. (Amazing!)
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

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


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed(list):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    count = 0
    for letter in secret_word:
        if letter in list:
            count = count + 1
    if count == len(secret_word):
        return True
    else:
        return False


def print_guessed(list):
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    current_word = ['_']*len(secret_word)
    i = 0
    while i < len(secret_word):
        if secret_word[i] in lower(join(list,'')):  #Turning into a string and putting in lowercase. To make possible uppercase guesses.
            current_word[i] = secret_word[i]     #'_' in current word will be substituted by some letter, if there is.
        i=i+1
    return join(current_word,'')   #Outputing not the list, but the string.

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    print "Type 15 --> Easy level - 15 guesses!"
    print "Type 10 --> Medium level - 10 guesses!"
    print "Type 6 --> Hard level - 6 guesses!"
    level = input("What level do you want to play? ")
    i = 0
    if (level==15 or level==10 or level==6):          #Making just my levels permitted.
        MAX_GUESSES = level
    else:
        return "You typed an invalid level!"
    print  "You have %s guesses left" %(MAX_GUESSES)  #You have 6 guesses left. In the first time
    print_hangman_image(6 - MAX_GUESSES)
    list = []
    letter = raw_input("What is your letter? ")
    list.append(letter)    
    while i < len(list) :   #Going through the letters the user guessed. List of letters.  List of length 7. i goes from 0 to 6
        
        if list[i] not in list[:i]:                                  #If the letter was not cited in the previous letters.
            print print_guessed(list[:i+1])                          #Print how far the user knows the word. i+1 to begin with [0:1] and finish with [0:7] with list of length 7.
                                                                     #this make print_guessed be tested for all the slice of letters in the list.
            MAX_GUESSES = MAX_GUESSES - 1                            
            if (word_guessed(list[:i+1])==True):
                return "YOU WON THE GAME"  #If the list so far has already found the word. The user won the game.
                     
            print  "You have %s guesses left" %(MAX_GUESSES)
            print_hangman_image(6 - MAX_GUESSES)

            if (MAX_GUESSES == 0):
                return "GAME IS OVER"              #If the chances are over. Game is Over.            
            letter = raw_input("What is your next letter? ")
            list.append(letter)
        else:  #In case the letter is in the previous list, the user already typed this letter. No guesses. 
            print "You already guessed this letter"
            print "You have %s guesses left" %(MAX_GUESSES)
            letter = raw_input("What is your next letter? ")
            list.append(letter)
        i = i + 1
    return None
 
