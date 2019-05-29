import math

def get_speed():
    speed = input('Enter driver speed: ')

    try:
        check_limit(float(speed))
    except:
        print('Please enter an number speed.\n')

    return get_speed()

def check_limit(speed):
    over_limit = speed - 55

    if over_limit < -55:
        print('Vehicle is driving backwards.')
    elif over_limit == -55:
        print('Vehicle is stopped.')
    elif over_limit > -55 and over_limit <= -20:
        print('Vehicle is driving too slowly.')
    elif over_limit > -20 and over_limit <= 0:
        print('OK')
    else:
        print(get_points(over_limit))

def get_points(mph_over):
    points = math.ceil(mph_over/5)
    if points < 12:
        return 'Points: ' + str(points)
    else:
        return 'License Suspended!'

if __name__ == '__main__':
    get_speed()
