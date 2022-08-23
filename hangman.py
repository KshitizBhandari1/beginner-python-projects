#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 23 08:55:23 am

@author: kshitizbhandari

Hangman
"""
import random


def welcome():
    '''
    Prints the name of the game and welcomes the user
    '''
    print('''
     _   _                                          
    | | | |                                         
    | |_| | __ _ _ ___  __ _ _ __ ____  __ _ _ ___  
    |  _  |/ _` | '_  \/ _` | '_ ` _  \/ _` | '_  \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | | 
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                        __/ |                       
                       |____/                                 
    ''')
    print('Welcome to the game, Hangman!')
          

def gameStatus(life_left):
    '''
    Assumes life_left is an integer between 1 and 8
    
    Returns strings which when printed represent pictorial status of the hangman game.
    '''
    #asserting valid number of lives 
    assert 1 <= life_left and life_left <= 8, "Invalid number of lives"
    
    HANGMAN_PICS = ['''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
        ===''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     |   |
     O   |
    /|   |
         |
        ===''', '''
     +---+
     |   |
     O   |
     |   |
         |
        ===''', '''
     +---+
     |   |
     O   |
         |
         |
        ===''', '''
     +---+
     |   |
         |
         |
         |
        ===''','''
     +---+
         |
         |
         |
         |
        ===''']
        
    # return the image representing the number of lives left 
    return HANGMAN_PICS[life_left - 1]
    

def gameWWon():
    '''
    Returns graphic for when the user wins the game
    '''
    return '''
                 *     ,MMM8&&&.            *      
                      MMMM88&&&&&    .             
                     MMMM88&&&&&&&                 
         *           MMM88&&&&&&&&                 
                     MMM88&&&&&&&&                 
                     'MMM88&&&&&&'                 
                       'MMM8&&&'      *    _     
        '     |\___/|                      \\    
             =) ^Y^ (=   |\_/|             ||  '   
              \  ^  /    )a a '._.------.  //      
               )===(    =\T_= /    ~  ~  \//       
              /     \     ` `\   ~   / ~  /        
              |     |         |~   \ |  ~/         
             /| | | |\         \  ~/- \ ~\         
             \| | |_|/|        || |  // /`         
      _/\_/\_/'_/\ \_/'\_/'\_/((_/'((/'\\/'\_/\_/\_
      |  |  |   | \_)   |   |   |   |   |   |  |  |   
      |  |  | C | O | N | G | R | A | T | S |  |  |
      |  |  |   |   |   |   |   |   |   |   |  |  |
      |  |  | Y | O | U |   | W | O | N | ! |  |  |
      |  |  |   |   |   |   |   |   |   |   |  |  |
    '''
    
    
def gameLost():
   '''
   Returns graphic for when the user loses the game 
       (i.e. fails to guess the word correctly)
   '''
   return '''
   ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼┼
   ┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼┼
   ┼┼██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼┼
   ┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼┼
   ┼┼███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼┼┼
   ┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼
   ┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼┼┼
   ┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼
   ┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼┼┼
   ┼┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼   
   '''


def loadWords(filename):
    '''
    filename : string, name of a file
    Takes a file and returns a list of valid words.
        (Words are strings of lowercase letters.)
    
    Depending on the size of the word list, this function may take a while
    '''
    print('Loading word list from file...')
    
    file = open(filename, 'r')
    # line: string
    line = file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    print('  ', len(wordlist), 'words loaded.')
    file.close()
    
    return wordlist


def chooseWord(wordlist):
    '''
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)


def isWordGuessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word that the user is trying to guess
    letters_guessed: list, what letters have been guessed so far
    
    Returns:
        a boolean value
        True if all the letters of secret_word are in letters_guessed
        False otherwise
    '''
    test = True
    for a in secret_word:
        if a not in letters_guessed:
            test = False
            break
    return test


def getGuessedWord(secret_word, letters_guessed):
    '''
    secret_word: string, the word that the user is trying to guess
    letters_guessed: list, what letters have been guessed so far
    
    Returns a string comprised of letters and underscores that represents
        what letters in secret_word have been guessed so far
    '''
    # initialize to keep track of word state
    s = ''
    
    # iterate through the word to be guessed
    for letter in secret_word:
        # include the letter if it has been guessed
        if letter in letters_guessed:
            s = s + letter + ' '
        
        # otherwise keep the underscore
        # to represent a letter space left to be filled
        else:
            s = s + '_ '
    
    # return the state of the word with letters guessed so far
    return s










   
    
   
    
   
    
   
    
   