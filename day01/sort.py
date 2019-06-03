def sort(num1, num2, num3):
    if num2 < num1:
      sort(num2, num1, num3)
    elif num3 < num1:
      sort(num3, num1, num2)
    elif num3 < num2:
      sort(num1, num3, num2)
    else:
      return print([num1, num2, num3])

def get_numbers():
    numbers = input('Please enter 3 numbers separated by a space: ')
    
    try:
        num_list = numbers.split(' ') # convert input to list of 3 numbers
        sort(float(num_list[0]), float(num_list[1]), float(num_list[2])) # convert numbers to float & sort
        return get_numbers()
    except:
        print('Error: Please enter exactly 3 numbers separated by a single space.')
        return get_numbers() # request new input on error

if __name__ == '__main__':
    get_numbers()
        
        

        
        
