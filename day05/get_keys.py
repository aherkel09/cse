def get_keys_from_value(data, value):
    keys = []
    for d in data:
        if data[d] == value:
            keys += [d]
    
    return str(value) + ' is paired with: ' + str(keys)

def get_data():
    dictionary = input('Please enter key/value pairs (e.g., key1: value1, key2: value2): ')
    value = input('Enter a value to see which keys it is paired with: ')

    try:
        data = {}
        key_val = dictionary.split(', ')

        for k in range(len(key_val)):
            split = key_val[k].split(': ')
            data[split[0]] = split[1]

        print(get_keys_from_value(data, value))
    except Exception as error:
        print('Error:', error)
        get_data()
    
if __name__ == '__main__':
    get_data()
