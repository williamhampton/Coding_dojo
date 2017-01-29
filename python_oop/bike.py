import random
class bike(object):
    def __init__(self,price, max_speed):
        self.price = 200
        self.max_speed = 300
        self.miles = 0

    def riding(self):
        print 'Riding'
        self.miles += 10
        return self
    def reverse(self):
        print 'Reverse'
        if self.miles == 0:
            self.miles = 0
        else:
            self.miles -= 5
        return self
    def displayinfo(self):
        print ('Price: {} Max Speed: {} Miles: {}').format(self.price,self.max_speed,self.miles)
        return self

test = bike(0,0)
test.riding()
test.displayinfo()
test.reverse()
test.displayinfo()
test.riding().displayinfo().riding().displayinfo()
