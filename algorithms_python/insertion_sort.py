#use insertion sort to sort an array

array = [1,35,23,77,42]

def insertion(arr):
    for i in range(0,len(arr)):
        value = arr[i]
        loc = i
        while loc>0 and arr[loc-1]> value:
            arr[loc] = arr[loc-1]
            loc = loc-1
        arr[loc] = value
    print arr

insertion(array)
