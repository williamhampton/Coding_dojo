# create a class that adds and subtracts a variable number of arguments
# and prints the answer

class mathdojo:
    def __init__(self,data):
        self.data = data
    def add(self,ad, *add):
        for i in range(0, len(add)):
            self.data = self.data + add[i]
        self.data = self.data + ad
        return mathdojo(self.data)
    def sub(self,subt,*subtract):
        for i in range(0, len(subtract)):
            self.data = self.data - subtract[i]
        self.data = self.data- subt
        return mathdojo(self.data)
    def result(self):
        print self.data

mathdojo(8).add(10,10).sub(3,5).result()
