import datetime

def get_year_65(age):
    years_remaining = 65 - age
    current_year = datetime.date.today().year
    return current_year + years_remaining

def get_name_and_age(error=False):
    if error:
        print('\nPlease use only letters for your name & integers for your age.\n')
        
    name = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    try:
        year_65 = get_year_65(int(age))
        return show_response(str(name), year_65)
    except:
        return get_name_and_age(error=True)

def show_response(name, year):
    if year < datetime.date.today().year:
        tense = 'turned'
    else:
        tense = 'will turn'

    print(name + ', you ' + tense + ' 65 in the year ' + str(year) + '.\n')
    return request_restart()

def request_restart():
    restart = input('Start again? (y/n): ')
    if restart.lower() == 'y':
        return get_name_and_age()
    else:
        return False

if __name__ == '__main__':
    get_name_and_age()
        
        
        
