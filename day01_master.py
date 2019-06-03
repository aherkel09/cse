from day01 import year_65, max_numbers, summer_winter

operations = {
    1: ('Find out when I will turn 65', year_65.main()),
    2: ('Get the maximum of 2 numbers', max_numbers.main()),
    3: ('summer_winter', summer_winter.main()),
    4: ('Check driver speed', driver_speed.main()),
    5: ('See the odds & evens below a number', even_odd.main()),
    6: ('See the multiples of 3 & 5 below a number', multiples.main()),
    7: ('Check if a number is prime', check_prime.main()),
    8: ('See all the prime numbers below a number', primes.main()),
    9: ('See a sorted list of 3 numbers', sort.main()),
    10: ('Check if a number is a perfect number', perfect_number.main())
}

def get_operation():
    for key, value in operations.items():
        print(key, ':', value[0])
        
    selected = input('Enter the number of the operation you would like to perform: ')
    
    try:
        operations[selected][1]
    except:
        print('Error: Please enter a valid selection.')

if __name__ == '__main__':
    get_operation()
