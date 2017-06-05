# create a function contains that will tell if a value is in the queue

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
            return 'confusion'
list = Node(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)

print list.contains(8)
print list.contains(2)
