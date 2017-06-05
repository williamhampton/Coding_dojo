#return the product of ints from 1 to num

def factorial(num):
    if num < 1:
        print 0
        return 0
    total = 1
    while num > 1:
        total = num * total
        num -= 1
    print total
    return total

factorial(5)
