#@classMethod can be used to change the attributes of class which static Method cannot do 
#can be done by these ways for changing Class attributes from a Method(functions In Class)
                                        #ClassName.name = name
                                        #self.__class__.name = name
                                        #@classmethod can also be used
class Person:
    name = "Anonymous"
    # def ChangeName(self,name):
    #     self.__class__.name = name
    
    # def ChangeName(self,name):
    #     Person.name = name
    
    @classmethod
    def ChangeName(cls,name): #cls is not self it is explicitly refer to class
        cls.name = name
    
p1 = Person()
p1.ChangeName("Taha")
print(p1.name)
print(Person.name)