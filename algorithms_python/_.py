# recreate some of the _ library: map, reduce, find, filter, reject

class _:
    def map(self,arr, fun):
        for i in range(0,len(arr)):
            arr[i] = fun(arr[i])
        return arr
    def reduce(self,arr):
        x = 0;
        for i in range(0,len(arr)):
            x += arr[i]
        return x
    def find(self, arr, test):
        for i in range(0,len(arr)):
            if test(arr[i]) != 0:
                return arr[i]
    def filter(self,arr,test):
        a = [];
        for i in range(0,len(arr)):
            if test(arr[i]) != 0:
                a.append(arr[i])
        return a
    def reject(self, arr):
        for i in range(0,len(arr)):
            if arr[i] == True:
                return True





print _().map([1,2,3], lambda x: x*3)
print _().reduce([1,2,3])
def testing(val):
    if val%2 == 0:
        return val;
print _().find([1,2,3,4],lambda x: x%2 == 0)
print _().filter([1,2,3,4],lambda x:x%2 == 0)
print _().reject([False,'lambda', 1,None])
