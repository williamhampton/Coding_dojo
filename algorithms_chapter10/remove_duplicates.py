# create a function that removes duplicate letters and punctuation from a string
# and returns the result

def removeduplicate(string):
    arr = [string[0]];
    i = 1;
    while i <len(string):
        q = 0;
        while q < len(arr):
            if string[i] != arr[q] and q == len(arr)-1:
                arr.append(string[i]);
                i +=1;
                q = 0;
            if string[i] == arr[q]:
                i+=1;
                q = 0;
            if i >= len(string):
                string = ''.join(arr)
                print string
                return string
            if string[i] != arr[q]:
                q +=1;

removeduplicate('asdfasdf this is a test')
