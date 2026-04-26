# as we know class is a blueprint let say a bag factory have some requirements like material,zip etc these requirements are called (class)
#but they dont know which material they will use or how many zips they will attach so these things will be provided according to company and these companies are called OBJECTS
class Factory:
    a=12 
    def hello(self):
        print("how are you")
#if we call a class in any variable that variable is called OBJECT
obj=Factory()        
#now we can access anything from gthe lass using the onjects
print(obj.a) 
obj.hello() #so multiple objects can be created like this