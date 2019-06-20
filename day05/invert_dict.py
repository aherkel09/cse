def invert_dict(data):
    inverted = {}
    
    for d in data:
        if data[d] not in inverted:
            inverted[data[d]] = [d]
        else:
            inverted[data[d]] += [d]
    
    return inverted

def get_data():
    dictionary = input('Please enter key/value pairs (e.g., key1: value1, key2: value2): ')
    
    try:
        data = {}
        key_val = dictionary.split(', ')

        for k in range(len(key_val)):
            split = key_val[k].split(': ')
            data[split[0]] = split[1]

        print(invert_dict(data))
    except Exception as error:
        print('Error:', error)
        get_data()
    
if __name__ == '__main__':
    get_data()
