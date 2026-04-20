# Type Conversion in Python

# 🔹 What is Type Conversion?
# Converting one data type into another

# --------------------------------
# IMPLICIT TYPE CONVERSION
# --------------------------------
# Python automatically converts type

a = 5        # int
b = 2.5      # float

c = a + b    # int → float automatically
print(c)     # 7.5
print(type(c))  # float

# --------------------------------
# EXPLICIT TYPE CONVERSION
# --------------------------------
# Manually converting using functions

# int()
x = "10"
y = int(x)
print(y)        # 10
print(type(y))  # int

# float()
a = 5
b = float(a)
print(b)        # 5.0
print(type(b))  # float

# str()
num = 100
text = str(num)
print(text)        # "100"
print(type(text))  # str

# --------------------------------
# MORE EXAMPLES
# --------------------------------

# float to int
print(int(3.9))   # 3 (decimal removed)

# int to string
print(str(25))    # "25"

# string to float
print(float("3.14"))  # 3.14

# --------------------------------
# IMPORTANT NOTES
# --------------------------------

# 1. int() removes decimal (no rounding)
# 2. Invalid conversion gives error
# print(int("abc"))  # ERROR

# 3. str() can convert any type to string
# 4. float() can convert int or numeric string

# --------------------------------
# PRACTICE
# --------------------------------

a = "50"
b = 20

result = int(a) + b
print(result)   # 70
