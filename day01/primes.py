def get_primes(limit):
    primes = [2]
    count = 2

    while count < limit:
        if count not in primes and prime.check_prime(count):
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
    import check_prime as prime
    get_number()
else:
    from day01 import check_prime as prime
