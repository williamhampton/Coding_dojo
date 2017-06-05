#create a function that returns the sum of a number from 1 to that number
# if num is less than zero, treat as zero
def rsigma(num):
    if num < 1:
        print 0
        return 0
    total = 0
    while num >=1:
        total += num
        num -= 1
    print total
    return total
rsigma(3)
rsigma(rsigma(4))
