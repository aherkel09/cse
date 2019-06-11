def integer():
  n = int(input("enter an integer greater than 1: "))
  sum = 0
  for i in range(1,n + 1):
    sum = sum+i
  
  avg = sum/n
  print(avg)

integer()


  
  
  
