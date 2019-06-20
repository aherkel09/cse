def read_characters(text_file):
    alpha = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    alpha_dict = dict.fromkeys(alpha, 0)
    
    with open(text_file, 'r') as file:
        char_count = 0
        print('Reading characters...')
        
        while True:
            char = file.read(1)
            if not char:
                print('Finished. Read', char_count, 'character(s)')
                break
            elif char in alpha:
                char_count += 1
                alpha_dict[char] += 1
    
    for a in alpha_dict:
        print(a, alpha_dict[a])

def choose_file():
    files = {
        '1': ('lorem_ipsum.txt', '1000 words of nonsensical Latin text'),
        '2': ('leviathan_excerpt.txt', '4056 words from a scifi novel'),
    }

    print('Select A File:')
    for f in files:
        print(f, files[f])
    
    selected = input('Enter the number of the file you wish to analyze: ')

    try:
        read_characters(files[selected][0])
    except:
        print('Error: please enter a valid file selection.')
        choose_file()


if __name__ == '__main__':
    choose_file()
