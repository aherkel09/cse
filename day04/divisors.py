def get_divisors(x):
    divisors = []
    for i in range(1, x+1):
        if x % i == 0:
            divisors += [i]
    print(divisors)

def get_number():
    number = input('Please enter a number: ')

    try:
        get_divisors(abs(int(number)))
    except:
        print('Error: please enter only numbers')
        get_number()

if __name__ == '__main__':
    get_number()
