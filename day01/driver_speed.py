def get_speed():
    speed = input('Enter driver speed: ')

    try:
        get_points(float(speed))
    except:
        print('Please enter an number speed.\n')
        get_speed()
    
def get_points(speed):
    points = round(speed - 55) // 5
    
    if points < 1:
        print('OK')
    elif points < 12:
        print('Points:', str(points))
    else:
        print('License Suspended!')

if __name__ == '__main__':
    get_speed()
