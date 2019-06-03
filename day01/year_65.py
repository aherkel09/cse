import datetime

def get_year_65():
    fname = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    try:
        year_65 = datetime.date.today().year + (65 - int(age))
        print(fname + ', you will turn 65 in the year ' + str(year_65) + '.\n')
    except:
        print('Error: Please use only letters for your name & numbers for your age.\n')
        get_year_65()

if __name__ == '__main__':
    get_year_65()
