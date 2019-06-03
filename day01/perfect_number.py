def is_perfect_number(num):
    if num < 0:
        return print('\n') # no result if num < 0
        
    count = 1
    sum_divisors = 0
    
    while count < num:
        if num % count == 0:
            sum_divisors += count
        count += 1
    
    if sum_divisors == num:
        return print(num, 'is a perfect number\n')
    else:
        return print(num, 'is not a perfect number\n')

def get_number():
    num = input('Please enter a positive integer: ')

    try:
        is_perfect_number(int(num)) # convert to int & check number
    except:
        print('Please enter only positive integers\n')
        get_number() # request new input on error

if __name__ == '__main__':
    get_number()
