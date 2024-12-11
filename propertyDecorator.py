#The @property decorator in Python makes a method act like an attribute. It lets you access a method without calling it explicitly (no parentheses). It's useful for dynamic calculations or derived data, while keeping code clean, intuitive, and allowing controlled access to object properties.
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    @property
    def Percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+ "%"
    @Percentage.setter
    def Percentage(self,value): #setter method will not let set percentage directly
        raise AttributeError("Cannot Set Percentage Directly")

stu1 = Student(90,90,85)
print(stu1.Percentage)
stu1.phy = 55
print(stu1.Percentage)
stu1.Percentage = 45