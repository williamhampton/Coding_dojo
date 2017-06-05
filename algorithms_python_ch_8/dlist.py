# construct a basic double linked list class
#push pop back contains and size functions included

class dnode:
    def __init__(self,initdata):
        self.data = initdata
        self.prev = None
        self.next = None
    def contains(self,value):
        runner = self
        while(runner.data != value and runner != None):
            runner = runner.next
            if runner == None:
                return False
        if runner.data == value:
            return True
        else:
            print 'Danger Will Robinson'
            return False
    def push(self,data):
        runner = self
        while runner.next != None:
            runner = runner.next
        runner.next = dnode(data)
        runner.next.prev = runner
    def pop(self,info):
        if self.contains(info)== False:
            print 'the data is not in the set'
            return False
        else:
            runner = self
            while runner.data != info:
                runner = runner.next
            runner.prev.next = runner.next
        self.show()
    def show(self):
        runner = self
        array = []
        while( runner != None):
            array.append(runner.data)
            runner = runner.next
        print ("data: {}").format(array)
    def back(self):
        runner = self
        while runner.next != None:
            runner = runner.next
        print runner.data
        return runner.data
    def size(self):
        size = 0
        runner = self
        while runner != None:
            runner = runner.next
            size += 1
        print size
        return size
list = dnode(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)


list.pop(4)
list.size()
