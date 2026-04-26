#its basically the parameterrs for class 
#a constructor is the method that runs automatically when we call a class and this construtor function will target the object location
class Factory:
    #def __init__(self):
     #   pass ,this is the synatax for initializing here self gives the location where the parameters will be stored and parameters can be added by writing the side of self
     def __init__(self,materials,zips,pockets):
          self.materials=materials
          self.zips=zips
          self.pockets=pockets
     def show(self): #this wwill basically give a structured output
          print(f"Your object details are:- material={self.materials},number of zips={self.zips},number of pockets={self.pockets}")     
#Factory() ,if we call directly it will give errors so write the parameters inside
#Factory("leather",4,6)    
#now making object>>>>
reebok=Factory("leather",4,6)  #rebook have every acces of factory
#self is targeting location of reebok ,the all the data given by reebok is stored in self
campus=Factory("nylon",4,4)
print(reebok.pockets)
print(campus.pockets)
print(reebok.zips)
reebok.show()