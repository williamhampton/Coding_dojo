def insert_val_at(index, my_list, value):
    if (index > len(my_list)):
        return False
    else:
        newlist = []
        for i in range(0, len(my_list)):
            if (i == index):
                newlist.append(value)
                for x in range(index, len(my_list)):
                    newlist.append(my_list[x])
                return newlist
            else:
                newlist.append(my_list[i])
    pass
#list = [1,2,3,4,5]
#print insert_val_at(2,list,100)
