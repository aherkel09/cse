def get_average(limit):
    sum = 0
    for i in range(1, limit + 1):
        sum += i

    avg = sum / limit
    return avg

def get_number():
    number = input("Please enter an integer greater than 1: ")

    try:
        print(get_average(abs(int(number))))
    except:
        print('Error: please enter only positive integers greater than 1')
        get_number()

if __name__ == '__main__':
    get_number()
    
