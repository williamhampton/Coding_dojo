# create a function that censors words in a string given the string and an array of naughty words
# ie: give: 'snap crackle pop nincompoop',['crack', 'poop'] -->
# 'snap xxxxxle pop nincomxxxx'

def censorship(string, arr):
    newarr = [];
    i = 0;
    while i < len(string):
        for q in range(0, len(arr)):
            if string[i] != arr[q][0] and string[i] != arr[q][0]:
                newarr.append(string[i]);
                i += 1;
            if string[i] == arr[q][0]:
                naughty = [];
                for w in range(0, len(arr[q])):
                    naughty.append(string[i+w]);
                naughty = [''.join(naughty)];
                if naughty[0] == arr[q]:
                    for e in range(0,len(naughty[0])):
                        newarr.append('X');
                    i = i + len(naughty[0]);
                else:
                    newarr.append(string[i]);
                    i+=1;
    string = ''.join(newarr);
    print string;
    return string;
censorship('snap crackle pop nincompoop',['crack', 'poop'])
