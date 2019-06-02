import datetime

def get_name_and_age():
    name = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    try:
        get_year_65(int(age))
        return get_name_and_age()
    except:
        print('Error: Please use only letters for your name & numbers for your age')
        return get_name_and_age()

def get_year_65(age):
    year_65 = datetime.date.today().year + (65 - age)
    print(name, ', you will turn 65 in the year ', str(year_65), '.')

if __name__ == '__main__':
    get_name_and_age()
