def is_palindrome(string):
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
  
