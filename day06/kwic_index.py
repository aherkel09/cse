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

def get_kwic_index():
    print('Reading text from "leviathan_excerpt.txt"...')
    
    kwic = {}
    words = []
    longest = 0 # used for formatting output
    
    with open('lorem_ipsum.txt', 'r') as file:
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

    for s in sorted_indices:
        line = ''
        if len(kwic[s][0]) < longest:
            line += ' ' * (longest - len(kwic[s][0]))
        for w in kwic[s]:
            line += w
        
        print(line, '...')
        
    return kwic

def get_word(kwic):
    word = input('Enter a word to see its context: ')

    try:
        if len(word) > 3:
            line = ''
            for w in kwic[word]:
                line += w
            print(line)
        else:
            print('Error: Search word must be longer than 3 characters')
            get_word(kwic)
    except Exception as error:
        print('Error:', error)
        get_word(kwic)
    
if __name__ == '__main__':
    kwic = get_kwic_index()
    get_word(kwic)
