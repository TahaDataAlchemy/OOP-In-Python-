# Method -> class me jo functions hote hai onke methods khete hai 

class Student:
    def __init__(self,name,maths,english,sci):
        self.name = name
        self.maths = maths
        self.english = english
        self.sci = sci
    
    @staticmethod # TThis is used where we dont need self and any argument to pass into a function 
    def hello():
        print("Hello Class Result Hass Been Announced")
    def average_Marks(self):
        sum = 0
        lst = [self.maths,self.sci,self.english]
        for val in lst:
            sum+=val
        avg = sum/3
        return f"Hi {self.name} your avg marks: { round(avg,2)}"
   
    def get_marks(self):
        return {
            "Maths":self.maths,
            "English":self.english,
            "Sci":self.sci
        }       

s1 = Student("Karan",91,85,87)
print(s1.average_Marks())
print(s1.get_marks())

s1.hello()
s1.name = "TonyStark"
print(s1.average_Marks())
