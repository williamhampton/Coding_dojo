# given two sorted arrays return an array with the union of the two without any dupes

def nodupes(arr1, arr2):
    i = 0;
    q = 0;
    new = [];
    if len(arr1)< len(arr2):
        while i < len(arr1):
            if arr1[i] == arr2[q]:
                repeated = False;
                if len(new) == 0:
                    new.append(arr1[i]);
                    i+=1;
                    q +=1;
                else:
                    z = 0;
                    while z <len(new) and repeated == False:
                        if new[z] == arr1[i]:
                            repeated = True;
                            i +=1;
                            q +=1;
                        elif z == len(new)-1 and repeated == False:
                            new.append(arr1[i]);
                            i+=1;
                            q +=1;
                            repeated = True;
                        elif new[z] != arr1[i]:
                            z +=1;
            else:
                if arr1[i]< arr2[q]:
                    i +=1;
                elif arr2[q] < arr1[i]:
                    q +=1;
    if len(arr2)< len(arr1):
        while i < len(arr2):
            if arr2[i] == arr1[q]:
                repeated = False;
                if len(new) == 0:
                    new.append(arr2[i]);
                    i+=1;
                    q +=1;
                else:
                    z = 0;
                    while z <len(new) and repeated == False:
                        if new[z] == arr2[i]:
                            repeated = True;
                            i +=1;
                            q +=1;
                        elif z == len(new)-1 and repeated == False:
                            new.append(arr2[i]);
                            i+=1;
                            q +=1;
                            repeated = True;
                        elif new[z] != arr2[i]:
                            z +=1;
            else:
                if arr2[i]< arr1[q]:
                    i +=1;
                elif arr1[q] < arr2[i]:
                    q +=13
    return new;
array1 = [1,2,2,4,5]
array2 = [1,2,2,5,6,7,8]
print nodupes(array2, array1)
