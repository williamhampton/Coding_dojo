import random
def cointoss():
    heads = 0
    tails = 0
    for x in range (0,5000):
        randomnum = random.random()
        x = round(randomnum)
        if (x== 0):
            print ("This is Tails")
            tails += 1
            print ("Number of tails {}, Number of heads {}".format(tails,heads))
        if (x== 1):
            print ("This is Heads")
            heads += 1
            print ("Number of tails {}, Number of heads {}".format(tails,heads))
cointoss()
