def get_multiples(limit):
    if limit <= 0 or limit >= 1000: # defined on {0 < limit < 1000}
        return print('Please choose a positive number less than 1000\n')
    
    index = 0
    sum_multiples = 0
    while index <= limit:
        if index % 3 == 0 or index % 5 == 0:
            sum_multiples += index
        index += 1
    return print(sum_multiples)

def get_number():
    limit = input('Please enter a number: ')
    
    try:
        get_multiples(int(limit)) # verify input can be converted to int
    except:
        print('Error: Please enter only integers\n')
        get_number() # request new input on error
    
if __name__ == '__main__':
    get_number()
