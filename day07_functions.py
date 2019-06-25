def set_functions():
    from day07 import binary_search
    
    functions = {
        1: ('Perform a binary search on a set of 1000 random integers', binary_search.get_number),
    }

    return functions
