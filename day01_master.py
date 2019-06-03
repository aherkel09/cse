from day01 import (
    year_65, max_numbers, summer_winter, driver_speed, even_odd,
    multiples, check_prime, primes, sort, perfect_number
)

functions = {
    1: ('Find out when you will turn 65', year_65.get_year_65()),
    2: ('Get the maximum of 2 numbers', max_numbers.get_max_of_numbers()),
    3: ('summer_winter', summer_winter.summer_winter()),
    4: ('Check driver speed', driver_speed.get_speed()),
    5: ('See the odds & evens below a number', even_odd.get_limit()),
    6: ('See the multiples of 3 & 5 below a number', multiples.get_number()),
    # 7: ('Check if a number is prime', check_prime.get_number()),
    # 8: ('See all the prime numbers below a number', primes.get_limit()),
    9: ('See a sorted list of 3 numbers', sort.get_numbers()),
    10: ('Check if a number is a perfect number', perfect_number.get_number())
}

print('Day01 Functions:')
for key, value in functions.items():
    print(key, ':', value[0])

def get_function():        
    selected = input('Enter the number of the function you would like to run: ')
    
    try:
        functions[selected][1]()
        return get_function()
    except:
        print('Error: Please enter a valid selection.')
        return get_function()

if __name__ == '__main__':
    get_function()
