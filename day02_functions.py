def set_functions():
    from day02 import (
        palindrome, fibonacci
    )

    functions = {
        1: ('See if a string is a palindrome', palindrome.get_string),
        2: ('List the Fibonacci numbers up to a limit', fibonacci.get_number),
        11: ('Exit', 'exit'),
    }

    return functions
