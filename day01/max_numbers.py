def get_max_of_numbers():
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('Error: Please enter only numbers\n')
        return get_max_of_numbers()
        
    if num1 == num2:
        print(num1, 'is equal to', num2, '\n')
    elif num1 > num2:
        print(num1, '\n')
    elif num2 > num1:
        print(num2, '\n')
    
    return get_max_of_numbers()

if __name__ == '__main__':
    get_max_of_numbers()
