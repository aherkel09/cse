def add_member(members):
  member = input("Please enter a member's name (or type 'stop' to exit): ")

  if member != 'stop':
    members += [member]
    return add_member(members)
  else:
    print(members)

if __name__ == '__main__':
  add_member([])
