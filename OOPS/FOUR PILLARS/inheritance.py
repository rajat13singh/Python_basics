#<<<<<<<<INHERITANCE>>>>>>
#property or any possession that come to an heir(vaaris)
#iheritance works between classes i.e it allows class(child class) to inherit properties and behaviours(attributes and methods) from another class (parent class)
#benefits:- code reuabilty,organised structure,easy to maintain extend
class Factorymumbai(): #parent class#superclass
    a="i am an attribute mentioned inside factory"
    def hello(self):
        print("hello i am a method mentioned inside the factory")
class Factorypune(Factorymumbai):#also called subclass #this will be child class as this inherit the data of mumbai factory which is parent class
    pass    #this class has power that its objects can have power i.e data access of his parent class
obj1=Factorymumbai()
#this object can access all the attributes and methods of factory mumbai but cant access factory pune   
obj2=Factorypune()
obj2.hello() #so object2 can access factory of mumbai infact he is object of a pune class
