# given a number show the amount of change you would be able to
# produce using dollars, quarters,dimes, nickels, pennies

def changemaker(num):
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    finished = []
    while num >= 100:
        num -= 100
        dollars += 1
    while num >= 25:
        num -= 25
        quarters += 1
    while num >= 10:
        num -= 10
        dimes += 1
    while num >= 5:
        num -= 5
        nickels +=1
    while num > 0:
        num -= 1
        pennies += 1
    print ('Dollars: {}, Quarters: {}, Dimes: {}, Nickels: {}, Pennies {}'.format(dollars,quarters,dimes,nickels,pennies))

changemaker(366)
