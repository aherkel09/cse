def get_odd_numbers(num_list):
    odd_list = []
    for i in num_list:
        if i.isdigit():
            if int(i) % 2 != 0:
                odd_list.append(i)
    print(odd_list)

def get_odd_indices(user_list):
    odd_list = [user_list[u] for u in range(len(user_list)) if u % 2 != 0]
    print(odd_list)

def get_list():
    choice = input('Type 1 to see the odd NUMBERS in a list, or 2 to see the odd INDICES of a list: ')

    if choice == '1':
        function = get_odd_numbers
    elif choice == '2':
        function = get_odd_indices
    else:
        print('Please enter a valid selection.')
        return get_list()

    item_list = input('Please enter a list of items separated by a comma: ').split(', ')

    try:
        function(item_list)
    except Exception as error:
        print('Error:', error)
        get_list()

if __name__ == '__main__':
    get_list()
