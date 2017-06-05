# insertion sort algorithm

def insertionsort(arr):
  for i in range( 1, len(arr)):
    temp = arr[i]
    q = i
    while q > 0 and temp < arr[q - 1]:
        arr[q] = arr[q - 1]
        q -= 1
    arr[q] = temp
array = [1,4,2,5,7,4,3]
insertionsort(array);
print array
