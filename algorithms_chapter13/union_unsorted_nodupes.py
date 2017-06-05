# create a function that combines two arrays and returns an array with the combined elements
# given {(2,7,2,1), (6,7,2,6)} return {2,7,1,6} in any order

def combine(arr1, arr2):
    newarr = []
    i = 0;
    while i <len(arr1):
        con = True
        q = 0;
        while con == True and q < len(arr2):
            if arr1[i] == arr2[q]:
                i+=1;
                con = False;
                q = 0;
            if q == len(arr2)-1:
                newarr.append(arr1[i]);
                i+=1;
                con = False;
                q = 0;
            else:
                q+= 1;
    i = 0;
    while i<len(arr2):
        con = True;
        while con == True and q < len(newarr):
            if arr2[i] == newarr[q]:
                i +=1;
                con = False;
                q = 0;
            if q == len(newarr)-1:
                newarr.append(arr2[i]);
                i+=1;
                con = False;
                q = 0;
            else:
                q+= 1;
    return newarr
array1 = [2,7,2,1]
array2 = [6,7,2,6]
print combine(array1, array2);
