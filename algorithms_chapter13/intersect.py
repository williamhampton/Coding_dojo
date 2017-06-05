# given two sorted arrays, combine the two in a multiset intersection of the two
# ie: given [1,2,2,2,7] and [2,2,6,6,7] return [2,2,7]

def intersection(arr1, arr2):
    i = 0;
    q = 0;
    newarr = []
    if len(arr1)<=len(arr2):
        while i < len(arr1):
            if arr1[i] == arr2[q]:
                newarr.append(arr1[i]);
                i +=1;
                q +=1;
            else:
                if i < len(arr1):
                    if arr1[i] < arr2[q]:
                        i+=1;
                if q < len(arr2):
                    if arr2[q]<arr1[i]:
                        q+=1;
    if len(arr2)<=len(arr1):
        while i < len(arr2):
            if arr2[i] == arr1[q]:
                newarr.append(arr2[i]);
                i +=1;
                q +=1;
            else:
                if i < len(arr2):
                    if arr2[i] < arr1[q]:
                        i+=1;
                if q < len(arr1):
                    if arr1[q]<arr2[i]:
                        q+=1;
    return newarr;

array1 = [1,2,2,2,7];
array2 = [2,2,6,6,7];
print intersection(array1, array2);
