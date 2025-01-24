'''
Implement a word guessing game, such that when initialized with a dictionary and a target word,
the user can enter guesses, and the system indicates whether the guess is correct or not, and provide hints to help the user guess.

Solution:  cast
Guess:     cash
Hint:      111-

Solution:  cast
Guess:     salt
Hint:      01-1

Assumptions:
- dictionary given to us, 4 letter words

1) char in word and correct position
2) char in word but not correct position
3) char not in word

cast -> set('c', 'a', 's', 't')

cash


'''
import random
# dictionary = {"face", "cast", "tree", "tool"}
# target = dictionary[0]

class WordGame:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.target = random.sample(self.dictionary, 1)
        self.targetCharSet = set(self.target)
    




