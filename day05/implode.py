def implode(string):
    chars = ''
    for s in string:
        if s not in chars:
            chars += s
    
    return chars

def get_string():
    string = input('Please enter a string: ')
    
    try:
        print(implode(string))
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    get_string()
