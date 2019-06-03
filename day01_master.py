from day01 import (
    year_65, max_numbers, summer_winter, driver_speed, even_odd,
    multiples, #check_prime, primes, <-- pending completion
    sort, perfect_number
)

functions = {
    1: ('Find out when you will turn 65', year_65.get_year_65),
    2: ('Get the maximum of 2 numbers', max_numbers.get_max_of_numbers),
    3: ('Summer/Winter', summer_winter.summer_winter),
    4: ('Check driver speed', driver_speed.get_speed),
    5: ('See the odds & evens below a number', even_odd.get_limit),
    6: ('See the multiples of 3 & 5 below a number', multiples.get_number),
    # 7: ('Check if a number is prime', check_prime.get_number), <-- pending completion
    # 8: ('See all the prime numbers below a number', primes.get_limit), <-- pending completion
    9: ('See a sorted list of 3 numbers', sort.get_numbers),
    10: ('Check if a number is a perfect number', perfect_number.get_number),
    11: ('Exit')
}

print('Day01 Functions:\n')
for key, value in functions.items():
    print(key, ':', value[0]) # print function number & name

def get_function():
    selected = input('\nEnter the number of the function you would like to run: ')

    if selected == '11':
        raise SystemExit
    
    try:
        function_tuple = functions[int(selected)] # get function to run from dict
        run_function(function_tuple)
    except ValueError: # catch errors from user input
        print('Error: Please enter a valid selection')
        return get_function()
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
        get_function()
    else:
        print('Please enter "y" to restart or "n" to choose a new function\n')
        request_restart(function)

if __name__ == '__main__':
    get_function()
    
