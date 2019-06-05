def add_member(members):
    member = input("Please enter a member's name (or type 'done' to exit): ")

    if member != 'done':
        members += [member]
        return add_member(members)
    else:
        return print('Members:', members)

if __name__ == '__main__':
    add_member([]) # intitialize members as empty list
