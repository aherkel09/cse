import os

def quick_sort(word_list):
    less_than = []
    pivots = []
    greater_than = []
    
    if len(word_list) <= 1:
        return word_list
    else:
        pivot = word_list[0]
        for w in word_list:
            if w < pivot:
                less_than.append(w)
            elif w == pivot:
                pivots.append(pivot)
            elif w > pivot:
                greater_than.append(w)

    less = quick_sort(less_than)
    greater = quick_sort(greater_than)

    return less + pivots + greater

def get_kwic_index(print_request):
    print('Reading text from "lorem_ipsum.txt"...')
    
    kwic = {}
    words = []
    longest = 0 # used for formatting output
    
    filepath = os.getcwd() + '\\day06\\lorem_ipsum.txt'
    
    with open(filepath, 'r') as file:
        for line in file:
            words += [word for word in line.split()]
    
    for w in range(len(words)):
        before = ''
        after = ''
        
        if len(words[w]) > 3:
            if w > 0:
                before = words[w - 1] + ' '
                if len(before) > longest: # use longest first word to align text
                    longest = len(before)
            if w < (len(words) - 1):
                after = ' ' + words[w + 1]
                
            kwic[words[w]] = [before, words[w], after]

    sorted_indices = quick_sort(list(kwic.keys()))
    
    if print_request: # only requested on first run of function
        for s in sorted_indices:
            line = ''
            if len(kwic[s][0]) < longest:
                line += ' ' * (longest - len(kwic[s][0]))
            for w in kwic[s]:
                line += w

            print(line, '...')

    return kwic

def get_word(print_index=True):
    kwic = get_kwic_index(print_index)
        
    word = input('Enter a word to see its context: ')

    try:
        if len(word) > 3:
            line = ''
            for w in kwic[word]:
                line += w
            print(line)
        else:
            print('Error: Search word must be longer than 3 characters')
            get_word(print_index=False) # get data, but don't print again
    except Exception as error:
        print('Error:', error)
        get_word(print_index=False)
    
if __name__ == '__main__':
    get_word()
