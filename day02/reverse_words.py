def reverse_words(string):
    words = string.split(' ')
    reverse = ''
    
    for i in range(1, len(words)+1):
        reverse += words[0-i] + ' '
    
    return reverse

def get_string():
    string = input('Please enter a string of words: ')
    
    try:
        print(reverse_words(string))
    except Exception as error:
        print('Error:', error)
        get_string()
        
if __name__ == '__main__':
    get_string()
    
