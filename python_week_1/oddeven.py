def oddeven(a,b):
    while a < b:
        if a%2 == 0:
            print ("Number is {} This is and Even number".format(a))
            a+=1
        if a%2 != 0:
            print ("Number is {} This is an Odd number".format(a))
            a+=1
oddeven(1,2001)
