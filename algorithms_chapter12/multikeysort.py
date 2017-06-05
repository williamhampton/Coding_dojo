# create a function to sort objects that have a firstname and lastname like a real dictionary

class name:
    def __init__(self,first,last):
        self.firstname = first;
        self.lastname = last;

john = name("John", "Smith")
rachel = name("Rachel", "Ghouly")
michelle = name("Michelle", "Taylor")
adam = name("Adam", "Lambert")
array = [john,rachel,michelle,adam]
def dictionaryfun(arr):
    arr.sort(key = lambda x:x.lastname);
dictionaryfun(array)
for i in range(0, len(array)):
    print"{} {}".format(array[i].lastname, array[i].firstname)
