def check_valid(password):
    valid = [False, False, False, False, False]
    
    if len(password) >= 6 and len(password) <= 16:
        valid[0] = True
        
        for p in password:
            if p.isdigit():
                valid[1] = True
            elif p.islower():
                valid[2] = True
            elif p.isupper():
                valid[3] = True
            elif p in ['$', '#', '@']:
                valid[4] = True
    
    if False not in valid:
        return print('Password is valid.')
    
    return get_password(invalid=True)

def get_password(invalid=False):
    if invalid:
        print(
            'Invalid. Password must contain 6-16 characters:',
            '\nOne lower (a-z)\nOne upper (A-Z)\nOne number (0-9)', 
            '\nOne special ($, #, @)',
        )
        
    password = input('Please enter a password: ')
    
    try:
        check_valid(password)
    except Exception as error:
        print('Error:', error)
        get_password()
    
if __name__ == '__main__':
    get_password()              
