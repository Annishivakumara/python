class Car:

    def setengine(self,engine):
        self.engine=engine

    def getengine(self):
        print(self.engine)

class Honda(Car):

    def setcarmodel(self, model):
        self.model=model

    def getcarmodel(self):
        print(self.model)

mycar=Honda()
mycar.setengine('EY-18')
mycar.setcarmodel('69x')
print("Car Details")
mycar.getengine()
mycar.getcarmodel()
