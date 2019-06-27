def set_functions():
    from day02 import (
        palindrome, fibonacci, reverse_words, club_members, grades,
        password, average, even_digits, dogs_age, next_date
    )

    functions = {
        1: ('See if a string is a palindrome', palindrome.get_string),
        2: ('List the Fibonacci numbers up to a limit', fibonacci.get_number),
        3: ('Print a string of words in reverse', reverse_words.get_string),
        4: ('Create a list of club members', club_members.add_member),
        5: ('See total & average grades', grades.add_grade),
        6: ('Check if your password is valid', password.get_password),
        7: ('Calculate the average of a set of numbers up to a limit', average.get_number),
        8: ('See all the numbers with only even digits up to a limit', even_digits.get_limit),
        9: ('Convert a dog\'s calendar age to dog years', dogs_age.get_age),
        10: ('Enter a date to see the date on the following day', next_date.get_start_date)
    }

    return functions
