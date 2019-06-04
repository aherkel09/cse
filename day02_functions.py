def set_functions():
    from day02 import (
        palindrome, fibonacci, reverse_words
    )

    functions = {
        1: ('See if a string is a palindrome', palindrome.get_string),
        2: ('List the Fibonacci numbers up to a limit', fibonacci.get_number),
        3: ('Print a string of words in reverse', reverse_words.get_string),
        11: ('Exit', 'exit'),
    }

    return functions
