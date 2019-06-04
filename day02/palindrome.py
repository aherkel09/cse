def is_palindrome(string):
    letters = list(string)
    backwards = ''
    for l in range(1, len(letters)+1):
        backwards += letters[0-l]
    print(string, '==', backwards + '?')

    if backwards == string:
        return True

    return False

def get_string():
    string = input('Please enter a string of characters: ')

    try:
        print(is_palindrome(string))
    except Exception as error:
        print('Error:', error)
        get_string()

if __name__ == '__main__':
    get_string()
