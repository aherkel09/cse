def is_even(num):
    while num > 0:
        digit = num % 10 # get last digit
        if digit % 2 != 0:
            return False
        num = num // 10 # remove last digit & start over
    return True

def get_limit():
    limit = input("enter a number: ")
    
    try:
        limit = int(limit)
        for i in range(1, limit + 1):
            if is_even(i) == True:
                print(i)
    except:
        print('Error: please enter only numbers')
        get_limit()

if __name__ == '__main__':
    get_limit()
