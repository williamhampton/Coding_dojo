class car(object):
    def __init__(self,price,speed,fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12
    def display_all(self):
        print ('Price: {}').format(self.price)
        print ('Speed: {}').format(self.speed)
        print ('Fuel: {}').format(self.fuel)
        print ('Mileage: {}').format(self.mileage)
        print ('Tax: {}%').format(self.tax)

Mercedes = car(150000, 150, 'full', 25)
Mercedes.display_all()
Ford = car('Too Much',50,'full',10)
Ford.display_all()
