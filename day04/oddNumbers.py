def odd_numbers(list):
    oddList = []
    for i in list:
        if i % 2 != 0:
            oddList.append(i)
    print(oddList)
