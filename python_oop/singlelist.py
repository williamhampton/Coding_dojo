class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
def printval(list):
    runner = list.head
    while(runner.next != None):
        print(runner.value)
        runner = runner.next
    print(runner.value)
#printval(list)

def addback(list, val):
    runner = list.head
    while(runner.next != None):
        print runner.value
        runner = runner.next
    print runner.value
    runner.next = Node(val)
    runner = runner.next
    print runner.value
#addback(list, 'end of list')

def addfront(list, val):
    runner = list.head
    newlist = SinglyLinkedList()
    newlist.head = Node(val)
    runner2 = newlist.head
    print newlist.head
    while (runner.next != None):
        runner2.next = runner
        print runner2.value
        runner = runner.next
        runner2 = runner2.next
    runner2.next = runner
    print runner2.value
    runner = runner.next
    runner2 = runner2.next
    runner2.next = runner
    print runner2.value
    runner = runner.next
    runner2 = runner2.next
#addfront(list, 'addfront')

def insertbefore(list, valfront,val):
    runner = list.head
    print runner.value
    while (runner.next.value != valfront):
        print runner.value
        runner = runner.next
    x = runner
    runner = Node(val)
    print runner.value
    runner = x
    while (runner.next != None):
        runner = runner.next
        print runner.value

#insertbefore(list, 'Chad', 'new val')

def insertafter(list, valafter, val):
    runner = list.head
    while (runner.next.value != valafter):
        print runner.value
        runner = runner.next
    print runner.value
    runner = runner.next
    print runner.value
    x = runner.next
    runner = Node(val)
    print runner.value
    runner = x
    while (runner.next != None):
        runner = runner.next
        print runner.value
    print runner.value

#insertafter(list, 'Chad', 'insert after')

def removenode(list, val):
    runner = list.head
    while (runner.value != val):
        print runner.value
        runner = runner.next
    runner = runner.next
    print runner.value
    while (runner.next != None):
        runner = runner.next
        print runner.value

#removenode(list, 'Chad')

def reverse(list):
    q = list.head
    x = list.head
    y = list.head
    end = list.head
    while (end.next != None):
        end = end.next
    print end.value
    while (y.next != None):
        while (x.next != end):
            x = x.next
        print x.value
        end = x
        y = y.next
        x = q
    

reverse(list)
