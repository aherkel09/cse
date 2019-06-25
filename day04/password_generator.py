import random
import string

def password():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    symbols = ['_', ',', '-']
    length = random.randint(8, 16)
    passwordString = ""
    while len(passwordString) < length:
        passwordString += getRandom(random.randint(0, 2),
                                    lower, upper, symbols)

    print(passwordString)


def getRandom(n, lower, upper, symbols):
    if n == 0:
        return symbols[random.randint(0, 2)]
    elif n == 1:
        return lower[random.randint(0, len(lower)-1)]
    else:
        return upper[random.randint(0, len(upper)-1)]
