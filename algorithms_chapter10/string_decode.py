# decode a string that has numbers and letters to show how many repeating letters
# there are ie: a3r4 --> aaarrrr
import re

def decode(string):
    array = []
    for i in range(0,len(string)):
        if re.search(r'\d', string[i]):
            dig = int(string[i])
            array.append(string[i-1]* dig)
    string = ''.join(array)
    print string;
    return string;

    string = ''.join(array)
    print string
    return string
decode('a1b2c3d4')
