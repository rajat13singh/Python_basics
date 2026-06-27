#ques3



class Student:

    def display(self, name, age=None, course=None):

        if age is None and course is None:
            print("Name:", name)

        elif course is None:
            print("Name:", name)
            print("Age:", age)

        else:
            print("Name:", name)
            print("Age:", age)
            print("Course:", course)


s = Student()

# Display only name
s.display("Rajat")

print()

# Display name and age
s.display("Rajat", 19)

print()

# Display name, age, and course
s.display("Rajat", 19, "B.Tech AIML")



#ques2



class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

# Add 2 numbers
print("Sum of 2 numbers =", calc.add(10, 20))

# Add 3 numbers
print("Sum of 3 numbers =", calc.add(10, 20, 30))

# Add 4 numbers
print("Sum of 4 numbers =", calc.add(10, 20, 30, 40))

 #ques1
class Addition:

    def add(self, a, b):
        print("Addition =", a + b)


class Subtraction:

    def subtract(self, a, b):
        print("Subtraction =", a - b)


class Multiplication:

    def multiply(self, a, b):
        print("Multiplication =", a * b)


class Calculator(Addition, Subtraction, Multiplication):
    pass


# Create object
c = Calculator()

# Perform operations
c.add(10, 5)
c.subtract(10, 5)
c.multiply(10, 5)

#add two boxes
class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight


b1 = Box(10)
b2 = Box(15)

print("Total Weight =", b1 + b2)
#compare students
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(85)
s2 = Student(78)

if s1 > s2:
    print("Student 1 has higher marks")
else:
    print("Student 2 has higher marks")


#add bank balances
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


acc1 = BankAccount(5000)
acc2 = BankAccount(7000)

print("Total Balance =", acc1 + acc2)

#areaa
class Area:

    def calculate_area(self, a, b=None):
        
        # Square
        if b is None:
            return a * a
        
        # Rectangle
        elif isinstance(b, (int, float)):
            return a * b
        
    # Triangle
    def calculate_area_triangle(self, base, height):
        return 0.5 * base * height


obj = Area()

# Square
print("Area of Square =", obj.calculate_area(5))

# Rectangle
print("Area of Rectangle =", obj.calculate_area(5, 4))

# Triangle
print("Area of Triangle =", obj.calculate_area_triangle(6, 8))


#####
#
