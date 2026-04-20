# Logical Operators in Python
# Used to combine conditions → result is True or False

a = 10
b = 5

# and → True if both conditions are True
print(a > 5 and b > 2)   # True
print(a > 5 and b > 10)  # False

# or → True if at least one condition is True
print(a > 5 or b > 10)   # True
print(a < 5 or b > 10)   # False

# not → reverses the result
print(not(a > 5))        # False
print(not(a < 5))        # True


# Using variables
x = True
y = False

print(x and y)   # False
print(x or y)    # True
print(not x)     # False


# Important notes
# and → both True
# or → at least one True
# not → opposite result