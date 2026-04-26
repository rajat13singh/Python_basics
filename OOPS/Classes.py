#oops is based on concepts of objects which contains data(attributes) and code(methods)
#class is like a blueprint or template for creating objects. 
#think calss is a blueprint of house and it contains rooms windows etc. but doesnt build the house .an object is the actual house built usingg that blueprint
#there are 2 types of thing inside class which attributes and methods
#attributes are rthe variables defined inside the class
#methods are the functions defined inside the class 
class Animal:
    species="Dog" #its a variable and inside a class so its called a attribute

    def make_sound(self): #this is the function inside the classs so its called the method
        print("bhaaau bhaaau!!!")
    print("Hello ,what are you doing?")
#now to call we have to call similar like functions
Animal() #this will initialized all the liness 
#but if we want to print the variables inside the class we have to call the class with variables ex Animal().species
print(Animal().species)
Animal().make_sound()        