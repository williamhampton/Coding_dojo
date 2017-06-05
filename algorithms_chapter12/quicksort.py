# create a quick sort function
array = [1,7,4,2,99,3,2,3]
def quicksort(arr):
    greater = [];
    equal = [];
    less = [];
    if len(arr)> 1:
        piviot = arr[0]
        for x in arr:
            if x < piviot:
                less.append(x)
            if x == piviot:
                equal.append(x)
            if x > piviot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater);
    else:
        return arr;
print quicksort(array)
