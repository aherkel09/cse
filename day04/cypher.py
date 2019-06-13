def advance_three_letters(string):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  caps = alpha.upper()
  advanced = ''

  for s in string:
    if s in alpha or s in caps:
      for a in range(len(alpha)):
        if alpha[a] == s and a <= 22:
          advanced += alpha[a + 3]
        elif alpha[a] == s:
          advanced += alpha[a - 23]
        elif caps[a] == s and a <= 22:
          advanced += caps[a + 3]
        elif caps[a] == s:
          advanced += caps[a - 23]
    else:
      advanced += s

  print(advanced)

def get_string():
  string = input('Please enter a string of letters & words: ')

  try:
    advance_three_letters(string)
  except Exception as error:
    print('Error:', error)
    get_string()

if __name__ == '__main__':
  get_string()
