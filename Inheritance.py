#Single Inheritance -> ek parent class and ek child class
#Multilevel Inheritance -> ek parent oska child then wo child ka child tu multilevel inheritance
#Multiple Inheritance -> ek class hai jiske ek se zaida parent hai tu wo ondono classes ki properties ko inherit karsakti hai 
class Car:
    @staticmethod
    def start():
        print("car Starts")

    @staticmethod
    def stop():
        print("car stops")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start() #-> Multilevel Inheritance


#Multiple Inheritance

class A:
    varA = "Welcome To class A"
class B:
    varB = "Welcome To class B"
class C(A,B):
    varC = "Welcome To class C"

c1 = C()
print(c1.varA)
print(c1.varA)
print(c1.varC)