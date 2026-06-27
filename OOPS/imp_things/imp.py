#Important Interview Questions
#Q1. Can a class have multiple constructors?
#
#No.
#
#class A:
#    def __init__(self):
#        print("First")
#
#    def __init__(self):
#        print("Second")
#
#Output:
#
#Second
#
#The second constructor overrides the first.
#
#Q2. Can we call constructor manually?
#
#Yes.
#
#class Student:
#    def __init__(self):
#        print("Hello")
#
#s = Student()
#
#s.__init__()
#
#Output:
#
#Hello
#Hello
#Q3. Is constructor mandatory?
#
#No.
#
#class Student:
#    pass
#
#s = Student()
#
#Valid code.