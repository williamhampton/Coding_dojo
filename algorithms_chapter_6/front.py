# create a method front to return the value at the front without removing it

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
    def front(self):
        return self.data
list = Node(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)

print list.front()
