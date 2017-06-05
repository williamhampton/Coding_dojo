# return the minimum of an array
array = [35,23,77,42,12,6]
def minsorted(arr):
    for i in range(0,len(arr)):
        value = arr[i]
        loc = i
        while loc>0 and arr[loc-1]> value:
            arr[loc] = arr[loc-1]
            loc = loc-1
        arr[loc] = value
    print arr[0]
    return arr[0]

minsorted(array)
