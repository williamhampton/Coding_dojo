# given two arrays that are already sorted, merge them into a new sorted array
# containing a multiset of all values.

def mergesort(arr1,arr2):
    i= 0;
    q = 0;
    newarr = []
    if len(arr1)< len(arr2):
        while i < len(arr1):
            if arr1[i]<= arr2[q]:
                newarr.append(arr1[i])
                i +=1;
            if q < len(arr2):
                if i != len(arr1):
                    if arr2[q]< arr1[i]:
                        newarr.append(arr2[q])
                        q +=1;
                if i == len(arr1):
                    while q <len(arr2):
                        newarr.append(arr2[q]);
                        q +=1;
    if len(arr2)< len(arr1):
        while i < len(arr2):
            if arr2[i]<= arr1[q]:
                newarr.append(arr2[i])
                i +=1;
            if q < len(arr1):
                if i != len(arr2):
                    if arr2[q]< arr2[i]:
                        newarr.append(arr1[q])
                        q +=1;
                if i == len(arr2):
                    while q <len(arr1):
                        newarr.append(arr1[q]);
                        q +=1;
    return newarr;

array1 = [1,2,3,3]
array2 = [1,3,4,5,6]
print mergesort(array2, array1)
