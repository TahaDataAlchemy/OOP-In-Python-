class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    @property
    def ShowDetails(self):
        return f"Role: {self.role}, Department: {self.dept}, Salary: {self.salary}"

class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        self.name = name
        self.age = age
        super().__init__(role, dept,salary)
    @property
    def ShowDetails(self):
        parentDetails = super().ShowDetails
        childDetails = f"Name: {self.name}, Age: {self.age}"
        return f"{childDetails}, {parentDetails}"

e1 = Engineer(name = "Taha",age = "25",role = "SoftwareEngineer",dept = "SoftwareDev",salary = "150K")
print(e1.ShowDetails)
