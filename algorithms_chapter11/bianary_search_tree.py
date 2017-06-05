# create a bianary search tree and create some basic functions for it
# ie: add, contains, max, min

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
test = tree(50)
test.add(40);
test.add(70);
test.add(30);
test.add(80);
test.add(75);
test.add(45);
test.add(76);
print test.contains(76)
print test.maxx()
print test.minn()
