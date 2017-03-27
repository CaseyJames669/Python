"""
Assignment 8:
***10.29 (Game: hangman) write a hangman game that randomly
generates a word and prompts the user to guess one letter
at a time. Each letter in the word is displayed as an asterisk.
When the user finishes a word, display the number of misses and
ask the user whether to continue playing.
"""

__author__="Casey Bladow"
__date__="11/20/12"

import random

#Word list - enter, delete, modify here to change words available
words = 'jack jim budweiser miller guiness barefoot honeyweiss'.split()

def getRandomWord(wordList):
    #Run through the word index and spits out the word
    #that the player must guess.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def game(missedLetters, correctLetters, secretWord):
    print()

    if missedLetters != '':
        print('Incorrect Letters:', end=' ')
        for letter in missedLetters:
            print(letter, end=' ')
        print()

    blanks = '*' * len(secretWord)

    #Replaces asterix's with correctly guessed letters
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    #show the hidden word with spaces inbetween each character
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns letter that the player entered.
    #ERROR CHECKING - makes sure a single letter was entered.
    #ERROR CHECKING - makes sure the guessed letter wasn't previously guessed.
    #ERROR CHECKING - makes sure ONLY a letter was entered.
    while True:
        print('Please guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('ERROR - Please only enter one letter at a time.')
        elif guess in alreadyGuessed:
            print('ERROR - You have already guessed that letter. Please choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('ERROR - Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #Ask user if they want to play again.
    #returns True if yes, False otherwise.
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')


print('Welcome to HANGMAN! Bar style ;)')
#initializing...
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    game(missedLetters, correctLetters, secretWord)

    #Let the player guess a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You got it. The hidden word was "' + secretWord + '"! Winner! Winner! Chicken Dinner!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Make sure the player hasn't guessed more than 6 times
        #Game Over, if so.
        if len(missedLetters) == 6:
            game(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nYou had ' + str(len(missedLetters)) + ' wrong guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    #Ask the player if they would like to play again
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
