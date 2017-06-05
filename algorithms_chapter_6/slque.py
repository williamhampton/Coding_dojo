# create a slque method that adds the given value to the end of our queue


class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def enqueue(self,data):
        self.next = Node(data)

list = Node(1)
list.enqueue(2)
print list.next.data
