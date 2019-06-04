def is_palindrome(string):
    letters = string.split('')
    backwards = ''
    for i in range(letters):
        backwards += letters[:i]
    print(backwards)
    
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
  
