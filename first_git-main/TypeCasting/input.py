# User Input in Python

# basic input
name = input("Enter name: ")
print(name)

# input is always string
print(type(name))   # str

# int input
age = int(input("Enter age: "))
print(age)
print(type(age))   # int

# float input
price = float(input("Enter price: "))
print(price)
print(type(price))   # float

# multiple input (same line)
a, b = input("Enter two values: ").split()
print(a, b)

# convert multiple input to int
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# comma separated input
x, y = map(int, input("Enter numbers: ").split(","))
print(x, y)

# important points
# input() returns string
# use int() or float() to convert
# split() is used for multiple values