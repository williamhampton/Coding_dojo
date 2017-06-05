# given a string and a number, rotate the string by said number
# ie: 'Boris Godunov' --> 'dunovBoris Go';

def rotate(string, num):
    arr = [];
    for i in range(len(string)-num, len(string)):
        arr.append(string[i]);
    for i in range(0,len(string)- num):
        arr.append(string[i]);
    string = ''.join(arr);
    print string;
    return string;

rotate('Boris Godunov', 5)
