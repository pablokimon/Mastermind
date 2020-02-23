# Requirements: Python 3 and an internet connection

'''
Mastermind is a command line game based on the boardgame of the same name.
This code was created as part of a seven day coding challenge in February 2020 by Paul Knowles
It does require an internet connection as it implements the random.org random integer generator to create the number combinations to be guessed.

'''

import requests
import json

def getRandomPattern(pattern_length,pattern_start,pattern_end):
    '''returns a list of a series of random numbers based on the parameters passed in.
    
    '''
    url = 'https://www.random.org/integers/' #integer generator
    params = {'num':pattern_length,'min':pattern_start,'max':pattern_end,'col':1,'base':10,'format':'plain','rnd':'new'} # api parameters
    response = requests.get(url,params) #save the contents of the get request to a variable
    pattern = response.text.strip('\n').split('\n') #parse the response into a nice list

    return pattern

def checkGuess(guess,pattern):
    '''compares a guess by the user to the computer's pattern. 
    This function expects both guess and pattern to lists of the same size.
    This similarity is checked when the guess is captured before it is passed here.
    We iterate through the guess from index 0.
    First we check for correct placement and correct number
    If not correct placement, then check if the guess is somehwere else in the pattern.'''
    
    correctPlace=0 #counter for number of guesses that are in the correct place and correct number
    correctNumber=0 #conter for the number of guesses that are only a correct number but NOT in the correct place.
    
    for x in range(len(guess)): #loops over the length of the guess, uses x as an index of the list

        if guess[x] == pattern[x]: #check if the index of the guess is in the correct place and correct number then increment counter
            correctPlace=+1 
        elif guess[x] in pattern: #if not correct location, check if the index of the guess is in the pattern at all and increment the counter
            correctNumber+=1
    return correctNumber,correctPlace #return the counts of correct number and place

def startGame():
    
    pattern_length = 4
    pattern_start = 1
    pattern_end = 8
    max_guess = 10
    
    print('''Welcome to MASTERMIND
    type \'set'\ to change game settings otherwise press enter to start!''')
    pattern = getRandomPattern(pattern_length,pattern_start,pattern_end)
    
    for m in range(1,max_guess):
        guess = input('Please enter %d numbers between %d and %d' %(pattern_length,pattern_start,pattern_end))
        guess=[int(g) for g in guess]
        checkGuess(guess,pattern)

if __name__ == "__main__":
    startGame()
    