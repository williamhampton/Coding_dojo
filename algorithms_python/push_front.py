# create a function that pushes a value to the front of an array
# without creating a new array

array = [1,2,3,4,5]
def pushpop(arr, val):
    arr.append(val)
    for x in range(0,len(arr)-1):
        arr[x],arr[len(arr)-1] = arr[len(arr)-1],arr[x]
    print arr
    return arr

pushpop(array, 0)
