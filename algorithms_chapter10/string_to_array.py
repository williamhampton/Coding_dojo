# create a function that turns a string into an array of words ie 'this is a test'=>
#['this', 'is', 'a', 'test']

def arraymaker(string):
    array = [];
    counter = 0;
    for i in range(0,len(string)):
        if string[i] == ' ':
            newarr = [];
            for q in range(counter, i):
                newarr.append(string[q])
            array.append(''.join(newarr))
            counter = i + 1 ;
        if i == len(string)-1:
            newarr = [];
            for q in range(counter, i+1):
                newarr.append(string[q])
            array.append(''.join(newarr))
    print array;
    return array;
arraymaker("this is a test")
