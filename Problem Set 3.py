import random


def loadWords():
    
    WORDLIST_FILENAME = "words.txt"
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
   
    line = inFile.readline()
    
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i in range(len(lettersGuessed)):
        if (lettersGuessed[i] in secretWord):
            count += 1
    
    if (count == len(lettersGuessed)):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

    Example Usage:

    >>> secretWord = 'apple' 
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'
    When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!

    For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.

    For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
    """
   
    s = ''
    for ch in secretWord:
        if ch in lettersGuessed:
            s += ch
        else:
            s += '_'
    
    return s
            
def getAvailableLetters(lettersGuessed):
   
    import string
    
    s = ''
    for c in string.ascii_lowercase:
        if not c in lettersGuessed:
            s += c
    
    return s
    
def hangman(secretWord):

    # FILL IN YOUR CODE HERE...

    numOfGuesses = 8
    lettersGuessed = []
    
    print("Welcome to the game Hangman!")
    print("The secret word is ", secretWord)
    print("I am thinking of a word that is ", len(secretWord), "letters long.")
    
    while (numOfGuesses > 0):
    	print("-----------")
    	print("You have ", numOfGuesses, " gusses left.")
    	print("Available Letters: ", getAvailableLetters(lettersGuessed))
    	guessInput = input("Please guess a letter: ")
    	if (guessInput not in secretWord):
    		print("Opps: That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
    		numOfGuesses -= 1
    	else:
    		print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
    	lettersGuessed.append(guessInput)
    	
    	if (isWordGuessed(secretWord, lettersGuessed) == True):
            print("-----------")
            print("Congratulations, you won!")
            return
    
    if (numOfGuesses == 0):
        print("\nSorry, you ran out of guesses. The word was ", secretWord)
        return
    
hangman(chooseWord(loadWords()))


