def get_multiples(limit):
    if limit >= 1000: # defined for integers <= 1000
        return print('Please choose a number less than 1000\n')
    count = 0
    while count <= limit:
        if count % 3 == 0 or count % 5 == 0:
            print(count)
        count += 1
    return print('Limit Reached\n')

def get_input():
    limit = input('Please enter a number: ')
    
    try:
        get_multiples(int(limit)) # verify input can be converted to int
        return get_input()
    except:
        print('Error: Please enter only integers\n')
        return get_input() # request new input on error
    
if __name__ == '__main__':
    get_input()
