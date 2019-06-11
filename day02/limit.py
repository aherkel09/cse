def test():
    limit = int(input("enter a number: "))
    for i in range(1, limit + 1):
        if isEven(i) == True:
            print(i)


def isEven(num): #500
    n = num 
    while n > 0:
        digit = n % 10 #0
        n = n // 10 #50
        if digit % 2 != 0:
            return False
    return True


test()
