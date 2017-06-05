# given a string of words, return a string of the words in order
# ie: this is a test --> test a is this

def reverse(string):
    arr = [];
    temparray = [];
    counter = 0;
    for i in range( 0 , len(string)):
        if string[i] == ' ':
            for q in range(counter, i):
                temparray.append(string[q]);
            arr.append(''.join(temparray));
            temparray = [];
            counter = i+1;
        if i == len(string)-1:
            for q in range(counter, i+1):
                temparray.append(string[q]);
            arr.append(''.join(temparray));
    for i in range(0, len(arr)/2):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i];
    string = ' '.join(arr);
    print string;
    return string;

reverse('this is a test')
