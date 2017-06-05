#create a function that sorts using selection sorts

array = [1,7,3,5,2,1]

def selection(arr):
    for x in range(0,len(arr)):
        for y in range(x, len(arr)):
            if arr[x] > arr[y]:
                arr[x],arr[y] = arr[y], arr[x]
    print arr
    return arr

selection(array)
