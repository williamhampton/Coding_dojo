# create a function to interleave two arrays untill one is exhausted then add everything
# from the other array

def interleave(arr1,arr2):
    i = 0;
    newarr = []
    while i<len(arr1):
        newarr.append(arr1[i]);
        if i< len(arr2):
            newarr.append(arr2[i]);
        i +=1;
    while i <len(arr2):
        newarr.append(arr2[i]);
        i+=1;
    return newarr;
array1 = [1,2,3,4,5,6];
array2 = [7,8,9,0];
print interleave(array2,array1);
