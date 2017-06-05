# given two strings return wheter one is a permutation of the other one
# ie ('mister', 'stimer') --> true ('mister', 'sister')--> false

def permutation(str1, str2):
    if len(str1) != len(str2):
        print False;
        return False;
    i = 0;
    q = 0;
    arr1 = [];
    arr2 = [];
    while i < len(str1):
        arr1.append(str1[i]);
        arr2.append(str2[i]);
        i += 1;
    i = 0;
    while i < len(arr1):
        while q < len(arr2):
            if arr1[i] == arr2[q]:
                arr1[i] = 0;
                arr2[q] = 0;
                i +=1;
                q = 0;
            if arr1[i] != arr2[q] and q == len(arr2)-1:
                print False;
                return False;
            if arr1[i] != arr2[q]:
                q +=1;
            if arr1 == arr2:
                print True;
                return True;

permutation('mister', 'stimer')
permutation('mister', 'sister')
