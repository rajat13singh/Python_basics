#Attributes are the variables which are defined inside the class
#there are two types of attributes >>>> class and instance
class Animal:
    name="lion" #its a {class attribute} ,a normal attribute created inside a class
    def __init__(self,age):
        self.age=age #so attribute which is created using self is known as {instance}
#methods are basically functions we created and these are three types>>>> instance
    def show(self):
        print(f"how are you,your age is {self.age}")
#class method
#this method works itself with the class and not target the instance(object)
# we have to use @classmethod and take its cls as its first parameter
    @classmethod #its a decorator method
    def hello(cls): #here cls will not interfere the objcts loction as it targets only class location
        print("hello bro!!")  
#static method: this doesnt access class or instance directly it also uses decorator @staticmethod , its just act as a regular fucntion placed inside a class
    @staticmethod
    def static():
        print("how are you")   
obj=Animal(23) #giving age to animal
obj.show()
obj.hello() #it will not work on age like cls.age>>it will not give anyhting
obj.static()