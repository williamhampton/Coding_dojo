# given an aray return wether the array contains that value using a divide and
#conquor method

import random
array = [1,2,3,4,5,6]

def arrayfunction(arr, val):
    i = random.randint(0,len(arr)-1)
    if val > arr[len(arr)-1]:
        print 'false'
        return False
    while i:
        if arr[i] > val:
            i = random.randint(0,i)
        if arr[i] == val:
            print 'True'
            return True
        if i < val:
            i = random.randint(i,len(arr)-1)
        if i == 0 and arr[i] != val:
            print 'False'
            return False
        if i == len(arr) and arr[i] != val:
            print 'False'
            return False


arrayfunction(array, 9)
arrayfunction(array, 3)
