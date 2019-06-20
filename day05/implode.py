def implode(string_list):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    imploded = []
    
    for string in string_list:
        chars = ''
        for a in alpha:
            if a in string and a not in chars:
                chars += a
        imploded += [chars]
    
    return imploded

def get_string():
    string_list = input('Please enter a list of strings separated by a comma: ')
    
    try:
        string_list = string_list.lower().replace(' ', '').split(',')
        print(implode(string_list))
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    get_string()
