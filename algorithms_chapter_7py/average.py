#create a function to produce the average of a set of numbers

def average(arr):
    x = 0
    counter = 0
    for i in range(0,len(arr)):
        x += arr[i]
        counter += 1
    print x/counter
    return x/counter

array = [2,4,6,8,10]
average(array)
