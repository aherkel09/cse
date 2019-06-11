def check_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    
    count = 2
    while count < num:
        if num % count == 0:
            return False
        count += 1

    return True

def get_primes(limit):
    primes = [2]
    count = 2

    while count <= limit:
        if count not in primes and check_prime(count):
            primes += [count]
        count += 1

    return print(primes)

def get_number():
    num = input('Please enter a number: ')

    try:
        get_primes(int(num))
    except:
        print('Please enter only positive integers\n')
        get_number()

if __name__ == '__main__':
    get_number()
