class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def new(self,data):
        runner = self
        while(runner.next != None):
            runner = runner.next
        runner.next = Node(data)
        runner.next.prev = runner
        runner = self

    def contains(self,value):
        runner = self
        while(runner.data != value and runner != None):
            runner = runner.next
            if runner.next == None:
                return False
        if runner.data == value:
            return True
        else:
            return 'Danger Will Robinson'
    def size(self):
        x = 0
        runner = self
        while(runner != None):
            x +=1
            runner = runner.next
        return x
    def position(self, num):
        if self.size < num:
            return False
        x = 1
        runner = self
        while(x != num):
            runner = runner.next
            x +=1
        return runner.data
    def show(self):
        runner = self
        while( runner != None):
            print runner.data
            runner = runner.next
    def delete(self,val):
        if self.contains(val) != True:
            print "cannot delete what is not there"
            return False
        else:
            runner = self
            while runner.data != val:
                runner = runner.next
            runner.prev.next = runner.next
            runner.next.prev = runner.prev
        runner = self
        self.show()
        return self
list = Node(1)
list.new(2)
list.new(3)
list.new(4)
list.show()
list.delete(3)
