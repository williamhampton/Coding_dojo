# given two sorted arrays, create a union of the two ie:
# [1,2,2,2,7] and [2,2,6,6,7] ==> [1,2,2,2,6,6,7]

def union(arr1,arr2):
    i = 0;
    q = 0;
    newarr = []
    if len(arr1)< len(arr2):
        while i< len(arr1):
            if arr1[i] <= arr2[q]:
                newarr.append(arr1[i]);
                i +=1;
            else:
                if arr2[q] < arr1[i]:
                    newarr.append(arr2[q]);
                    q+=1;
        while q<len(arr2):
            newarr.append(arr2[q]);
            q+=1;
    if len(arr2)< len(arr1):
        while i< len(arr2):
            if arr2[i] <= arr1[q]:
                newarr.append(arr2[i]);
                i +=1;
            else:
                if arr1[q] < arr2[i]:
                    newarr.append(arr1[q]);
                    q+=1;
        while q<len(arr1):
            newarr.append(arr1[q]);
            q+=1;
    return newarr
array1 = [1,2,3,4,5];
array2 = [1,2,3,4,5,6,6];
print union(array2, array1)
