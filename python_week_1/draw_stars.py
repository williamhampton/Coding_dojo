def draw_stars(x):
    q = 0
    for i in range(len(x)):
        result = isinstance(x[q],int)
        if (result == True):
            number = x[q]
            star = "*"*number
            print star
            q+=1
        else:
            print x[q][0]
            q +=1

a = ["asdfe", "efra", 5, "rewiqkjl", "qweirojwq",12,3]
draw_stars(a)
