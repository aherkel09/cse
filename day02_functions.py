def set_functions():
    from day02 import (
        palindrome, fibonacci, reverse_words, club_members, grades,
        password
    )

    functions = {
        1: ('See if a string is a palindrome', palindrome.get_string),
        2: ('List the Fibonacci numbers up to a limit', fibonacci.get_number),
        3: ('Print a string of words in reverse', reverse_words.get_string),
        4: ('Create a list of club members', club_members.add_member),
        5: ('See total & average grades', grades.add_grade),
        6: ('Check if your password is valid', password.get_password),
        11: ('Exit', 'exit'),
    }

    return functions
