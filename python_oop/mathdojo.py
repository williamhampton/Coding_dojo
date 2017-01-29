class mathdojo(object):
    def __init__(self,*nums):
        self.answer = 0

    def add(self,*nums):
        for i in range (0, len(nums)):
            if(isinstance(nums[i], list) |  isinstance(nums[i], tuple)):
                for x in range(0, len(nums[i])):
                    self.answer += nums[i][x]
            else:
                self.answer += nums[i]
        return self

    def subtract(self, *nums):
        for i in range (0, len(nums)):
            if(isinstance(nums[i], list) |  isinstance(nums[i], tuple)):
                for x in range(0, len(nums[i])):
                    self.answer -= nums[i][x]
            else:
                self.answer -= nums[i]
        return self

    def result(self):
        print self.answer

mathdojo().add(5,[5,5]).subtract(10,5).result()
mathdojo().add(2).add(2, 5).subtract(3, 2).result() 
