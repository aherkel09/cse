def summer_winter(error=False):
    if error:
        print('Error: Please enter only numbers\n')
        
    num = input('Please enter a number: ')
    
    try:
        num = int(num)
    except:
        summer_winter(error=True)
        
    if num %3 == 0 and num % 5 == 0:
        print('SummerWinter')
    elif num % 3 == 0:
        print('Summer')
    elif num % 5 == 0:
        print('Winter')
    else:
        print(num)

    print('\n')
    return summer_winter()

if __name__ == '__main__':
    summer_winter()
