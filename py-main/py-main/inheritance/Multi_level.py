#Multilevel Inheritance
class Car:

    def setengine(self,engine):
        self.engine=engine

    def getengine(self):
        print("Engine Type:-",self.engine)

class Honda(Car):

    def setcarmodel(self, model):
        self.model=model

    def getcarmodel(self):
        print("Honda Model:-",self.model)

class Electric(Honda):

    def setkm(self, km):
        self.km=km

    def getkm(self):
        print("Speed per hour:-", self.km)

        
electric=Electric()
electric.setengine('EY-18')
electric.setcarmodel('69x')
electric.setkm("1500km")
print("-:Car Details:-")
electric.getengine()
electric.getcarmodel()
electric.getkm()
