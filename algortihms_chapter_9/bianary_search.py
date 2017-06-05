# create a recursive function that searches an array for a value

class search():
    def find(self,i,arr,val):
        if arr[i] == val:
            return True

    def stack(self,arr,val):
        for i in range(0,len(arr)):
            if self.find(i,arr,val) == True:
                return True
        return False

array = [1,2,3,4,5]
print search().stack(array,2)
