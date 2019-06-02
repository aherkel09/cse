import datetime

def get_name_and_age():
    name = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    try:
        get_year_65(float(age))
        return get_name_and_age()
    except:
        return get_name_and_age()

def get_year_65(age):
    year_65 = datetime.date.today().year + (65 - round(age))
    current_year = datetime.date.today().year
    print(name + ', you ' + tense + ' 65 in the year ' + str(year) + '.')

if __name__ == '__main__':
    get_name_and_age()
    
