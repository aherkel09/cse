import day01_functions

def get_functions():
    functions = {}
    print('Days: 01')
    day = input('Which day do you want to demonstrate?: ')

    if day == '01':
        day01.set_functions()
    else:
        return get_functions()

    print('\nFunctions:\n')
    for key, value in functions.items():
        print(key, ':', value[0]) # print function number & name
    
    return request_function()

def request_function():
    selected = input('\nEnter the number of the function you would like to run: ')

    if selected == '11':
        raise SystemExit
    
    try:
        function_tuple = functions[int(selected)] # get function to run from dict
        run_function(function_tuple)
    except ValueError: # catch errors from user input
        print('Error: Please enter a valid selection')
        return request_function()
    except: # catch any errors from selected function
        return request_restart(function_tuple)

def run_function(function_tuple):
    print(function_tuple[0]) # print function name
    try:
        function_tuple[1]()
    finally:
        return request_restart(function_tuple) # always ask user to restart
    
def request_restart(function):
    restart = input('Run function again? (y/n): ').lower()
    if restart == 'y':
        run_function(function)
    elif restart == 'n':
        request_function()
    else:
        print('Please enter "y" to restart or "n" to choose a new function\n')
        request_restart(function)

if __name__ == '__main__':
    get_functions()
    
