#Abstraction srf ye k zarori things visible ho only , like gari ka class bana kar osme sari functionalities defined kardo or user ko srf start ka method run karna ho 
#Implementation Hide kardo or user ko srf required details dekhao ->  Abstraction

#Encapsulation yehi hai jo implement kari wi hai like class oske andar data and feature 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def carStart(self):
        self.acc = True
        self.clutch = True

        print("Car Is Runing")

car1 = Car()
car1.carStart()
