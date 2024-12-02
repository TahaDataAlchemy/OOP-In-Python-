#Used to del object or any attribute using del (important For OOP)

class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student("Karan")

del s1

print(s1)
# through an error -> (name 's1' is not defined) because object id deleted
        