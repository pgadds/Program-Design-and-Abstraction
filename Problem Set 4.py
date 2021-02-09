#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:33:41 2019

@author: navboi
"""

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
   
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def getWordScore(word, n):

    score = 0 
    bonus = 50 
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter] 
    score *= len(word) 
    
    if n == len(word):
        score += bonus
    return score


def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       
    print()                            


def dealHand(n):
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    new_hand = dict(hand) 
    for letter in word:
        if letter in new_hand:
            new_hand[letter] -= 1 
    return new_hand

def isValidWord(word, hand, wordList):
    hand_cpy = dict(hand)
    word_count = getFrequencyDict(word)
    if word not in wordList:
        return False
    else:
        for element in word_count:
            if element not in hand_cpy or hand_cpy[element] < word_count[element]:
                return False
        return True
    
def calculateHandlen(hand):
   
    sum = 0
    for element in hand:
        sum += hand[element]
    return sum

def playHand(hand, wordList, n):
    total = 0
    while (calculateHandlen(hand) > 0):
        
  
        print('Current Hand:', end=' '); displayHand(hand)
        
        
        word = str(input('Enter word, or a "." to indicate that you are finished: '))
        
    
        if word is '.':
            break;
        else:
            if (not isValidWord(word, hand, wordList)):
                print ("Invalid word, please try again. \n")
            else:
                score = getWordScore(word, n)
                total += score
                print('"'+word+'"', "earned", score, "points. Total:", total, "points", '\n')
                hand = updateHand(hand, word)
        print('Goodbye! Total score:', total, 'points.')
    else:
        print('Run out of letters. Total score:', total, 'points.')  



def playGame(wordList):
    n_play_hand = 0
    while True:
        option = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if option is 'n':
            new_hand = dealHand(HAND_SIZE)
            playHand(new_hand, wordList, HAND_SIZE)
            n_play_hand += 1
        elif option is 'r':
            if n_play_hand is 0:
                print("You have not played a hand yet. Please play a new hand first!\n")
            else:
                playHand(new_hand, wordList, HAND_SIZE)
                n_play_hand += 1
        elif option is 'e':
            break;
        else:
            print("Invalid command.\n")


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    