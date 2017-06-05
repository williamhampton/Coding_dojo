# create a function that returns whether two queues are Identical
# as in same values in the same positions  return the queues at the end

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def enqueue(self,data):
        runner = self
        while(runner.next != None):
            runner = runner.next
        runner.next = Node(data)
        runner = self
    def dequeue(self):
        self.data = self.next.data
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
list = Node(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)
list2 = Node(1)
list2.enqueue(2)
list2.enqueue(3)
list2.enqueue(4)

def compare(que1, que2):
    if que1.size()< que2.size():
        return False, que1, que2
    if que1.size()> que2.size():
        return False, que1, que2
    for x in range(1, que1.size() +1 ):
        if que1.position(x) == que2.position(x):
            print '****'
        if que1.position(x) != que2.position(x):
            return False, que1, que2
        if x == que1.size():
            return True, que1, que2
print compare(list, list2)
