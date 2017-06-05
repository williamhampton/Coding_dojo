# create a standalone function to remove a linked lists minimum value

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
    def show(self):
        runner = self
        while( runner != None):
            print runner.data
            runner = runner.next
list = Node(1)
list.enqueue(2)
list.enqueue(3)
list.enqueue(4)

def removemin(que):
    x = que.data
    runner = que
    while(runner != None):
        if runner.data < x:
            x = runner.data
            runner = runner.next
        else:
            runner = runner.next
    if que.data == x:
        que = que.next
    newque = Node(que.data)
    que = que.next
    while(que != None):
        if que.data == x:
            que = que.next
        else:
            newque.enqueue(que.data)
            que = que.next
    newque.show()
    return newque
removemin(list)
