def set_functions():
    from day06 import read_characters, kwic_index
    
    functions = {
        1: ('See the distribution of letters in a text file', read_characters.choose_file),
        2: ('View & search the KWIC index of a text file', kwic_index.get_word),
    }
    
    return functions
