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
'''
import random

class WordGame:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.target = random.sample(sorted(self.dictionary), 1)[0]
        self.targetCharSet = set(self.target)
    
    def check(self, userGuess: str) -> str:
        res = []
        for i in range(len(userGuess)):
            if userGuess[i] in self.targetCharSet:
                if userGuess[i] == self.target[i]:
                    res.append("1")
                else:
                    res.append("0")
            else:
                res.append("-")
        return "".join(res)


def main(debug=False, mode="easy"):
    dictionaryUniverse = {
        "easy": set(["abe", "inu" ,"lin", "pow"]),
        "medium": set(["asdf", "oais", "qwer", "pkmi"]),
        "hard": set(["asdfas", "asdfas", "asdfas"])
    }

    dictionary = dictionaryUniverse[mode]
    wordLen = random.choice(dictionary)

    game = WordGame(dictionary)
    debugTarget = ""

    if debug == True:
        debugTarget = game.target
        print(debugTarget)

    while guessCount != 0:
        userGuess = input(f"What is your guess? (Must be {wordLen} characters): ")
        if len(userGuess) != wordLen:
            print("wrong character limit")
            continue
        checkResult = game.check(userGuess)
        if checkResult == "1111":
            print("Correct Guess!")
            return
        print(checkResult)
        guessCount -= 1

    print("You used all attempts")
    return

main(True)



