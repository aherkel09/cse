def get_fibonacci(limit):
    fibonacci = [1]
    index = 1
    while index <= limit:
        fibonacci += [index]
        index = fibonacci[-1] + fibonacci[-2]

    return fibonacci

def get_number():
    num = input('Please enter a number: ')

    try:
        print(get_fibonacci(int(num)))
    except:
        print('Error: Please enter only positive integers\n')

if __name__ == '__main__':
    get_number()
