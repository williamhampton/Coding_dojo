class Underscore(object):
    def __init__(self):
        self.ans = []
    def map(self,var,fun):
        for i in range(0, len(var)):
            self.ans[i] = fun(var[i])
        return self

    def reduce(self,var):
        newans = 0
        for i in range(0, len(var)):
            newans += var[i]
        self.ans.append(newans)
        for i in range(1, len(self.ans)):
            self.ans[i].remove()
        return self
    def find(self,var,fun):
        for i in range(0,len(var)):
            if (fun(var[i])):
                self.ans.append(var[i])
                return self
            else:
                continue
        return self
    def filter(self,var,fun):
        for i in range(0,len(var)):
            if (fun(var[i])):
                self.ans.append(var[i])
            else:
                continue
        return self

    def reject(self, var, fun):
        for i in range(0,len(var)):
            if (fun(var[i])):
                continue
            else:
                self.ans.append(var[i])
        return self
    def show(self):
        print self.ans

_ = Underscore()
#_.reduce([1,2,3,4,5]).show()
#_.find([1,2,3,4,5], lambda x: x%2 == 0).show()
#_.filter([1,2,3,4,5], lambda x: x%2 ==0).show()
#_.reject([1,2,3,4,5], lambda x: x%2 ==0 ).show()
