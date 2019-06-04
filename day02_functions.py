def set_functions():
    from day02 import (
        palindrome
    )

    functions = {
        1: ('See if a string is a palindrome', palindrome.get_string),
        11: ('Exit', 'exit'),
    }

    return functions
