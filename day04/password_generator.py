import random
import string

def generate_password():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    symbols = ['_', ',', '-']
    length = random.randint(8, 16)
    password_string = ""
    while len(password_string) < length:
        password_string += get_random(random.randint(0, 2), lower, upper, symbols)

    print(password_string)


def get_random(n, lower, upper, symbols):
    if n == 0:
        return symbols[random.randint(0, 2)]
    elif n == 1:
        return lower[random.randint(0, len(lower)-1)]
    else:
        return upper[random.randint(0, len(upper)-1)]

if __name__ == '__main__':
    generate_password()
