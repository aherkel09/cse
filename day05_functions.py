def set_functions():
    from day05 import (
        value_frequency, key_frequency, get_keys, invert_dict, implode,
    )

    functions = {
        1: ('Enter a dictionary & a value to see how frequently the value occurs', value_frequency.get_data),
        2: ('Enter a dictionary & a key to see how frequently the key occurs', key_frequency.get_data),
        3: ('Enter a dictionary & a value to see which keys are paired with that value', get_keys.get_data),
        4: ('Invert the keys & values of a dictionary', invert_dict.get_data),
        6: ('See the alphabetized characters of a string with no repeats', implode.get_string)
    }

    return functions
