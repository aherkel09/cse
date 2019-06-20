def set_functions():
    from day04 import (
        # odd_indices
        divisors, explode, cypher, #password_generator
        random_integers
    )

    functions = {
        # 1: ('Get the values of the odd indices of a list', odd_indices.get_list),
        2: ('See the divisors of a number', divisors.get_number),
        6: ('See a list of all the characters in a string', explode.get_string),
        7: ('Advance all the letters in a string by 3 letters', cypher.get_string),
        # 9: ('Generate a password', password_generator.generate_password),
        10: ('See the distribution of a million random integers between 0 and 100', random_integers.get_distribution)
    }

    return functions
