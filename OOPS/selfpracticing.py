###################################################PART C
#q1
class Student:
    def studentinfo(self,name,age):
        self.name=name
        self.age=age  
students=[]
for i in range(int(input("how many students:-"))):          
    s=Student()     
    s.name=input("enter your name:-")
    s.age=int(input("enter your age:-"))
    students.append(s)
for s in students:    
    print(s.__dict__)
#############################################    
class Car:
    def carinfo(self,model,colour,old):
        self.model=model
        self.colour=colour
        self.old=old
m=Car()
m.carinfo("mahindra","balck",2)    
print(m.__dict__)

