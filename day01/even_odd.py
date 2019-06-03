def even_odd(limit):
    if limit > 1000:
        return print('Please choose a number under 1000')
    count = 0

    while count <= limit:
        if count % 2 == 0:
            print(count, 'EVEN')
        else:
            print(count, 'ODD')
        count += 1

    return print('Limit Reached\n')

def get_limit():
    limit = input('Please enter a number: ')

    try:
        even_odd(int(limit))
        return get_limit()
    except:
        print('Error: Please use only integers')
        return get_limit()

if __name__ == '__main__':
    get_limit()
