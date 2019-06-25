import random

def get_random_numbers():
    random_ints = []
    for x in range(1000):
        rand = random.randint(5, 10005) # 5 - 10,005
        random_ints += [rand]
    
    return quick_sort(random_ints)

def quick_sort(num_list):
    less_than = []
    pivots = []
    greater_than = []
    
    if len(num_list) <= 1:
        return num_list
    else:
        pivot = num_list[0]
        for n in num_list:
            if n < pivot:
                less_than.append(n)
            elif n == pivot:
                pivots.append(pivot)
            elif n > pivot:
                greater_than.append(n)

    less = quick_sort(less_than)
    greater = quick_sort(greater_than)

    return less + pivots + greater

def binary_search(target):
    search_set = get_random_numbers()
    num_comparisons = 0
    lower = 5
    upper = 10005
    
    while(num_comparisons < 14):
        num_comparisons += 1
        middle = ((upper - lower)// 2) + lower
        if middle < target:
            lower = middle
        elif middle > target:
            upper = middle
        else:
            return 'Target ' + str(target) + ' found in ' + str(num_comparisons) + ' comparisons.'
      
    return 'Search failed. Please try again.'
        
def get_number():
    number = input('Please enter an integer between 5 & 10,005 (or type 0 to exit): ')
    
    try:
        number = int(number)
        if number >= 5 and number <= 10005:
            print(binary_search(number))
        elif number == 0:
            print('Goodbye')
        else:
            print('Error: Number must be between 5 & 10,005')
            get_number()
    except:
        print('Error: Please enter only numbers')
        get_number()

if __name__ == '__main__':
    get_number()
