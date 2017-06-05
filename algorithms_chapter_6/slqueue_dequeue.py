#create a function dequeue to remove and return the value at the front of a list


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

list = Node(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)

list.dequeue()
print list.data
