def dogs_age():
  dogs_age = int(input("Input a dog's age in human years: "))
  if dogs_age <= 2:
	  human_age = 10.5
  else:
	  human_age = 21 + (dogs_age - 2) * 4

  print("The dog's age in dog's years is: ", human_age)      

dogs_age()                 
