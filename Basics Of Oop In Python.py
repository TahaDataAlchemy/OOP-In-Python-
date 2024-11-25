#attribute = Any Variable
#Object = Person("Alice", 30)
#Class Attribute = These are common for all objects ,like all name belongs to same college
#Instance Attribute = There are seperate for all objects, like assigning name to each person   

#Object Attribute Precendence is Higher then Class Attribute, Mtlb Jab bhi do same name k attribute honge tu Object wala phela chale ga 

class  Student:
    # This Is Class Attribute

    College_Name = "ABC college"
    name = "Areej"
    #Default Construtor(wo function jisme srf self ho)
    def __init__(self):
        pass
         
    #Paramaterized Constructor (Jisme Self k ilawa bhi Parameters ho) 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

s1 = Student("Karen",35)
print(s1.name)
print(s1.marks)
print(s1.College_Name)
print(Student.College_Name)
