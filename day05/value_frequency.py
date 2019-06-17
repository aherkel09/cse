def get_frequency(data, value):
    freq = 0
    for d in data:
        if data[d] == value:
            freq += 1
    
    return str(value) + ' occurs ' + str(freq) + ' times.'

def get_data():
    dictionary = input('Please enter key/value pairs (e.g., key1: value1, key2: value2): ')
    value = input('Enter a value to see how frequently it occurs: ')

    try:
        data = {}
        key_val = dictionary.split(', ')

        for k in range(len(key_val)):
            split = key_val[k].split(': ')
            data[split[0]] = split[1]

        print(get_frequency(data, value))
    except Exception as error:
        print('Error:', error)
        get_data()
    
if __name__ == '__main__':
    get_data()
