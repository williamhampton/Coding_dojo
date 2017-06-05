# get all of the values at a certian layer of the bianary search tree

def quicksort(arr):
    greater = [];
    equal = [];
    less = [];
    if len(arr)> 1:
        piviot = arr[0]
        for x in arr:
            if x < piviot:
                less.append(x)
            if x == piviot:
                equal.append(x)
            if x > piviot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater);
    else:
        return arr;
def flat(arr):
    arr2 = []
    for i in range(0,len(arr)):
        if isinstance( arr[i], ( int, long ) ):
            arr2.append(arr[i])
        else:
            for x in range(0, len(arr[i])):
                arr2.append(arr[i][x])
    return arr2

class tree:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;
    def add(self, newdata):
        runner = self;
        while runner.data < newdata:
            if runner.right == None:
                runner.right = tree(newdata);4
                break;
            if runner.data < newdata:
                runner = runner.right
                runner.add(newdata)
            if runner.data > newdata:
                runner = runner.left
                runner.add(newdata)
        while runner.data > newdata:
            if runner.left == None:
                runner.left = tree(newdata);
                break;
            if runner.data < newdata:
                runner = runner.right
                runner.add(newdata)
            if runner.data > newdata:
                runner = runner.left
                runner.add(newdata)
    def contains(self, data):
        runner = self;
        while runner.data < data:
            if runner.right == None:
                runner.right = tree(data);4
                break;
            if runner.data < data:
                runner = runner.right
                runner.contains(data)
            if runner.data > data:
                runner = runner.left
                runner.contains(data)
        while runner.data > data:
            if runner.left == None:
                runner.left = tree(data);
                break;
            if runner.data < data:
                runner = runner.right
                runner.contains(data)
            if runner.data > data:
                runner = runner.left
                runner.contains(data)
        if runner.data != data:
            return False;
        else:
            return True;
    def maxx(self):
        runner = self
        while runner.right != None:
            runner = runner.right;
        return runner.data
    def minn(self):
        runner = self
        while runner.left != None:
            runner = runner.left;
        return runner.data
    def show(self):
        bst = self;
        def bsttoarray(bst):
            array = []
            array.append(bst.data)
            if bst.left != None:
                array.append(bsttoarray(bst.left));
            if bst.right != None:
                array.append(bsttoarray(bst.right));
            return quicksort(flat(array))
        return bsttoarray(bst)
    def layer(self,val):
        array = []
        def layerx(bst, val):
            arr = []
            if val == 0 and bst != None:
                arr.append(bst.data)
            if bst != None:
                if val >0 and self.left != None:
                    arr.append(layerx(bst.left, val-1));
                if val> 0 and self.right != None:
                    arr.append(layerx(bst.right, val-1));
            return flat(arr)
        return layerx(self,val)

test = tree(50);
test.add(40);
test.add(70);
test.add(30);
test.add(80);
test.add(75);
test.add(45);
test.add(76);
test.add(1);
test.add(24);
test.add(17);
test.add(27);
test.add(95);
test.add(56);
test.add(55);
test.add(77);
test.add(99);
test.add(176);
print test.layer(4)
