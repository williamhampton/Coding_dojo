class animal(object):
    def __init__(self):
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -=5
        return self
    def displayhealth(self):
        print ('Health: {}').format(self.health)
        return self

class dog(animal):
    def __init__(self):
        super(dog,self).__init__()
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class dragon(animal):
    def __init__(self):
        super(dragon,self).__init__()
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayhealth(self):
        print ('its a dragon!')
        print ('Health: {}').format(self.health)

basic = animal()
basic.walk().walk().walk().run().run().displayhealth()
puppy = dog()
puppy.walk().walk().walk().run().run().pet().displayhealth()
erigorn = dragon()
erigorn.walk().walk().walk().run().run().fly().fly().displayhealth()
randomanimal = animal()
#randomanimal.fly()
#randomanimal.pet()
