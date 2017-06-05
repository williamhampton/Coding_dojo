# calculate the greatest common factor of two numbers

class gcf():
    def divide(self,num,val):
        if num% val == 0:
            return True
    def greatest(self,num1,num2):
            if num1 >= num2:
                array = []
                for i in range(1,num2+1):
                    if self.divide(num1,i) and self.divide(num2,i) == True:
                        array.append(i)
            if num2 > num1:
                array = []
                for i in range(1,num1+1):
                    if self.divide(num1,i) and self.divide(num2,i) == True:
                        array.append(i)
            return array[len(array)-1]
print gcf().greatest(2,4)
print gcf().greatest(20,50)
print gcf().greatest(90,1000)
