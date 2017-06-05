# use recursion to use the find the nth number in
# the fibonacci sequence

class fib:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def new(self,data):
        runner = self
        while(runner.next != None):
            runner = runner.next
        runner.next = fib(data)
        runner = self
    def times(self,times):
        runner = self
        x = 1
        if times <= 0:
            print 0
            return 0
        if times == 1:
            print 0
            return 0
        while(x != times):
            x +=1
            self.new(runner.data + runner.next.data)
            runner = runner.next
        self.show()
    def show(self):
        runner = self
        while runner.next != None:
            runner = runner.next
        print runner.data
        return runner.data
q = fib(0)
q.new(1)
q.times(6)
