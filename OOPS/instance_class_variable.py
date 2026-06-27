#An instance variable is a variable whose value belongs to a specific object.
#accessing the instance variable
class Student:
    def __init__(self):
        self.name = "Rajat"

s = Student()

print(s.name)
#deleting the instance variables
class Students:
    def __init__(self):
        self.name = "Rajat"

s1 = Students()

del s1.name
if hasattr(s1, "name"):
    print(s1.name)
else:
    print("Attribute deleted")
#EVery object stores its insatnce variable in a dictionary
class Student:
    def __init__(self):
        self.name = "Rajat"
        self.age = 20

s = Student()

print(s.__dict__)
#imp
class Student:
    def __init__(self):
        self.x = 10

s1 = Student()
s2 = Student()

s1.x = 100

print(s1.x)
print(s2.x)
#Because instance variables belong to individual objects.
class Student:

    college="CGC"

Student.college="IIT"  #here it modify the class variable

#but if s.college="lpu" then its not modify it its create a seperate for this object only
s=Student()

print(s.college)