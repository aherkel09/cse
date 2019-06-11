def date():
    day31 = [1, 3, 5, 7, 8, 10, 12]
    year = int(input("Input a year: "))
    month = int(input("Input a month: "))
    day = int(input("Input a day: "))
    if month in day31 and day == 31 and month == 12:
        day = 1
        month = 1
        year = year + 1
    elif month in day31 and day == 31:
        day = 1
        month = month + 1
    elif month not in day31 and month == 2 and day == 28:
        month = month + 1
        day = 1
    elif month not in day31 and day == 30:
        month = month + 1
        day = 1
    else:
        day = day + 1
    print("The next date is: " + str(year) + "-" + str(month) + "-" + str(day))


date()
