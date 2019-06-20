import day01_functions, day02_functions, day04_functions, day05_functions

def get_functions():
    global functions
    functions = {}
    
    days = {
        '01': day01_functions,
        '02': day02_functions,
        '04': day04_functions,
        '05': day05_functions,
    }
    days_list = [k for k, v in days.items()]
    
    print('Days:', days_list)
    selected_day = input('Which day do you want to demonstrate? (Type "exit" to exit): ')

    if selected_day in days_list:
        functions = days[selected_day].set_functions() # get function data from dayXX_functions.py
    elif selected_day == 'exit':
        raise SystemExit
    else:
        return get_functions()

    print('\nFunctions:\n')
    for key, value in functions.items():
        print(key, ':', value[0]) # print function number & name
    
    return request_function()

def request_function():
    selected = input('\nEnter the number of the function you would like to run (or type "exit" to exit): ')

    if selected == 'exit':
        return get_functions()
    
    try:
        function_tuple = functions[int(selected)] # get function to run from dict
        run_function(function_tuple)
    except ValueError: # catch errors from user input
        print('Error: Please enter a valid selection')
        request_function()
    except Exception: # catch any errors from selected function
        request_restart(function_tuple)

def run_function(function_tuple):
    print(function_tuple[0]) # print function name
    function_tuple[1]()
    request_restart(function_tuple)
    
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
    
