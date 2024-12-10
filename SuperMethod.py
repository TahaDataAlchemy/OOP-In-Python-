#Super Use to Access the Parent class methods: agar mujhe child se parent me koi bhi value pass karani ho tu bhi super use hosakta hai 
#Super isliye use hota hai k hume expecially parent class k method ko invoke karna hota hai tu
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("start Car")
    
    @staticmethod
    def stop():
        print("Car Stop")

class Toyota(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start() # Now when call toyota it will return the value of start also 

car1 = Toyota("Prius","Electric")
print(car1.type)