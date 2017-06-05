#  use bubble sort to sort an array

array = [1,7,3,4,5,2,3,8]
def bubble(arr):
    unsorted = True;
    while unsorted == True:
        unsorted = False;
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i];
                unsorted = True;
bubble(array)
print array
