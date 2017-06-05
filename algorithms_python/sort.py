#create a function that sorts an array by size, smallest to largest

array = [1,2,5,3,7,1]

def sortme(arr):
    for x in range(0,len(arr)-1):
        for y in range(0,len(arr)-1):
            if arr[y] >= arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
    print arr
    return arr

sortme(array)
