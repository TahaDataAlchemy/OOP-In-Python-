#Iska mtlb ye hai k ek hi cheez ki multiple functionalities like 1 +2 = 3 or 'Taha' + 'Mehboob' = TahaMehboob

# Dunder function wo function hai jiske sath double underscore hota hai
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def ShowNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        NewReal = self.real + num2.real
        Newimg = self.img + num2.img
        return Complex(NewReal,Newimg)
    def __sub__(self,num2):
        NewReal = self.real -num2.real
        Newimg = self.img - num2.img
        return Complex(NewReal,Newimg)

num1 = Complex(3,4)
num1.ShowNumber()

num2 = Complex(4,7)
num2.ShowNumber()

# num3 = num1.add(num2) without Dunder Funtion aese call hoga
num3 = num1 + num2 # with dunder function aese call hoga
num3.ShowNumber() 

num4 = num1 - num2
num4.ShowNumber()