def explode(string):
    char_list = []
    for s in string:
        char_list += [s]
    
    return char_list

def get_string():
    string = input('Please enter a string: ')
    
    try:
        print(explode(string))
    except Exception as error:
        print('Error:', error)
        get_string()

if __name__ == '__main__':
    get_string()
