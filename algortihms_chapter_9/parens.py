# given a number of parens, return an array of strings with every possible combination
# of the order of parens
import random
def randomparen():
    if random.randint(0,1) == 0:
        return '('
    else:
        return ')'
def parens(num):
    arr = []
    for i in range(0, num):
        x = ['(']
        q = 1
        w = 0
        for r in range(1,num*2):
            if q == num:
                x.append(')')
                r  += 1
            if q == w:
                x.append('(')
            else:
                s = randomparen()
                if s == '(':
                    q +=1
                    x.append('(')
                else:
                    x.append(')')
                    w +=1
        arr.append(''.join(x))
    print arr
    return arr
parens(2)
