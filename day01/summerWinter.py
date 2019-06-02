def summer_winter():
    num = input('Please enter a number: ')
    
    try:
        num = int(num)
    except:
        print('Error: Please enter only numbers\n')
        summer_winter()
        
    if num % 3 == 0 and num % 5 == 0:
        print('SummerWinter\n')
    elif num % 3 == 0:
        print('Summer\n')
    elif num % 5 == 0:
        print('Winter\n')
    else:
        print(str(num) + '\n')

    return summer_winter()

if __name__ == '__main__':
    summer_winter()
