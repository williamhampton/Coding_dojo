# given a value k, return the kth value in a list


# given a dlist insert a value before an existing value

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
def prepend(l,val,before):
    runner = l
    if l.contains(before) == False:
        print 'cannot add before a value that does not exist'
        return False
    if l.data != before:
        l = dnode(runner.data)
        runner = runner.next
        while runner.data != before:
            l.push(runner.data)
            runner = runner.next
        l.push(val)
        while(runner != None):
            l.push(runner.data)
            runner = runner.next
        l.show()
        return l
    if runner.data == before:
       k = dnode(val)
       k.next = runner
       k.show()
       l = k
       return l
def  kvalue(l, k):
    if l.size<k:
        return False
    x = 0
    runner = l
    while x != k:
        runner = runner.next
        x+= 1
    print runner.data
    return runner.data
list = dnode(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
list = prepend(list,7,1)

kvalue(list, 2)
