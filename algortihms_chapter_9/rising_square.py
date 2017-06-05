#create a function that prints the square of every number including the square
# of the number itself

def rising(num):
    print num*num
    if num == 1:
        return num
    else:
        rising (num-1)
rising(9)
