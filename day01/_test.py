def sieve(num): 
    prime = [True for n in range(num+1)] 
    check = 2
    while ((check * check) <= num): 
        if (prime[check] == True): 
            for n in range(check * 2, num+1, check): 
                prime[n] = False
        check += 1
    print(prime)
    
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

    while count < limit:
        if count not in primes and check_prime(count):
            primes += [count]
        count += 1

    print(primes)

def get_number():
    num = input('Please enter a number: ')
    
    try:
        get_primes(int(num))
    except:
        print('Please enter only positive integers\n')
        get_number()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("get_primes(2000)", setup="from __main__ import get_primes", number=1))
    print(timeit.timeit("sieve(2000)", setup="from __main__ import sieve", number=1))
