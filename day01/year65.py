import datetime
import math

def get_name_and_age(error=False):
    if error:
        print('\nPlease use only letters for your name & integers for your age.\n')
        
    name = check_alpha(input('Please enter your first name: '))
    age = input('Please enter your age: ')

    try:
        year_65 = get_year_65(float(age))
        return show_response(name, year_65)
    except:
        return get_name_and_age(error=True)

def check_alpha(string):
    for s in string:
        if not s.isalpha():
            return get_name_and_age(error=True)
    return string

def get_year_65(age):
    years_remaining = 65 - round(age)
    current_year = datetime.date.today().year
    return current_year + years_remaining

def show_response(name, year):
    current_year = datetime.date.today().year
    
    if year < current_year:
        tense = 'turned'
    else:
        tense = 'will turn'

    message = name + ', you ' + tense + ' 65 in the year ' + str(year) + '.'

    if current_year - (year - 65) > 115 or current_year - (year-65) < 5:
        message += ' Seems unlikely.'

    print (message)
    return request_restart()

def request_restart():
    restart = input('Start again? (y/n): ')
    if restart.lower() == 'y':
        return get_name_and_age()
    else:
        print('Goodbye.')
        return

if __name__ == '__main__':
    get_name_and_age()
    
