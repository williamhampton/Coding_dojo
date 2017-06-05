# create a function that uses selection sort to sort an array
array = [12,4,7,2,5,9,2,6]
def selection(arr):
    for i in range(0,len(arr)):
        temp = i;
        for q in range(i,len(arr)):
            if arr[temp]>arr[q]:
                temp= q;
            if q == len(arr)-1:
                arr[i], arr[temp] = arr[temp],arr[i];

selection(array);
print array
