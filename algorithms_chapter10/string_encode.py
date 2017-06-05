# given a string of consecutive characters, shorten the string by the char and the number
# of times that it appears ie bbb --> b3.  If it is not shorter than the original string,
# return the original string

def shortener(string):
    counter = 1;
    i = 0;
    temp = []
    while i < len(string)-1:
        if i == len(string)-1:
            if string[i] != string[i+1]:
                temp.append(string[i]);
                temp.append(('{}').format(counter));
                counter = 1;
                i +=1;
            if string[i] == string[i+1]:
                i +=1;
                counter +=1
                temp.append(string[i]);
                temp.append(('{}').format(counter));
        if string[i] == string[i+1]:
            i +=1;
            counter +=1
        if string[i] != string[i+1]:
            temp.append(string[i]);
            temp.append(('{}').format(counter));
            counter = 1;
            i +=1;
    newstring = ''.join(temp)
    if len(newstring)< len(string):
        print newstring;
        return newstring;
    else:
        print string;
        return string;
shortener('aaabbbbbcccccddde')
