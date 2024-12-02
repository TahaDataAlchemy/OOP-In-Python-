#public(Method & Attr) -> can be accessed outside the class
#private(Method & Attr) -> cannot be accessed outside the class
#any attribute/Method needs to be private add underscore __accpass when called it should return error -> ('Account' object has no attribute '__acc_pass')
#Private Method/attr can be accessed inside the class like by other Function

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def __hello(self): # Private Method
        print("Hello World")
    
    def welcome(self): # Like this user can do welcome but not hello
        self.__hello()

    def reset_pass(self):
        print(self.__acc_pass) #-> Now it can be access as it is in the class and print statement in it 
acc1 = Account("12345","abcde")
print(acc1.reset_pass())
print(acc1.welcome())