def get_frequency(data, key):
    freq = 0
    for d in data:
        if d == key:
            freq += 1
    
    return str(key) + ' occurs ' + str(freq) + ' time(s).'

def get_data():
    dictionary = input('Please enter key/value pairs (e.g., key1: value1, key2: value2): ')
    key = input('Enter a key to see how frequently it occurs: ')

    try:
        data = {}
        key_val = dictionary.split(', ')

        for k in range(len(key_val)):
            split = key_val[k].split(': ')
            data[split[0]] = split[1]

        print(get_frequency(data, key))
    except Exception as error:
        print('Error:', error)
        get_data()
    
if __name__ == '__main__':
    get_data()
