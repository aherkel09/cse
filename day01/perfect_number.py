def is_perfect_number(num):
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
        is_perfect_number(abs(int(num))) # convert to int & check number
    except:
        print('Please enter only positive integers\n')
        get_number() # request new input on error

if __name__ == '__main__':
    get_number()
