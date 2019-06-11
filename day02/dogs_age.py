def get_dogs_age(years):
	if years <= 2:
		human_age = 10.5 * years
	else:
		human_age = 21 + (years - 2) * 4

	print("The dog's age in dog's years is", human_age)      

def get_age():              
	years = input("Input a dog's age in human years: ")
	
	try:
		get_dogs_age(int(years))
	except:
		print('Error: please enter only numbers')
		get_age()

if __name__ == '__main__':
	get_age()
