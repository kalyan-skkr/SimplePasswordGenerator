import random

from constants import Constants

with open(Constants.wordsfilepath) as f:
    wordList = (f.read()).split()

class PwdGenRepo:
    words = wordList

    def set_password_length(reqArgs):
        if 'length' in reqArgs:
            pwdLength = int(reqArgs['length'])
            if pwdLength < Constants.pwdMinLen:
                pwdLength = Constants.pwdMinLen
            if pwdLength > Constants.pwdMaxLen:
                pwdLength = Constants.pwdMaxLen
        else:
            pwdLength = Constants.pwdDefLen
        return pwdLength, pwdLength - Constants.nonAlphaNum

    def set_required_words(reqLetters, wordList):
        words = [x for x in wordList if len(x) == reqLetters // 2]
        oneword = False

        if len(words) == 0:
            words = [x for x in words if len(x) == reqLetters]
            oneword = True
        return words, oneword

    def genPass(words, oneword, specs):
        if oneword:
            firstPart = random.choice(words)
            secondPart = ''
        else:
            firstPart, secondPart = random.choices(words, k=2)
        specialChar1, specialChar2 = random.choices(specs, k=2)
        number = str(random.choice(Constants.numRange))

        password = firstPart.capitalize() + specialChar1 + secondPart.capitalize() + specialChar2 + number

        return password
