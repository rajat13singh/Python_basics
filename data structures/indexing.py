# What is Indexing?
# Indexing means accessing elements using position (index number)
# Index always starts from 0
# STRING INDEXING

text = "Python"

print("Original String:", text)

# Positive Indexing (Left to Right)
print("\nPositive Indexing:")
print(text[0])   # P
print(text[1])   # y
print(text[5])   # n

# Negative Indexing (Right to Left)
print("\nNegative Indexing:")
print(text[-1])  # n
print(text[-2])  # o
print(text[-6])  # P

# --------------------------------
# LIST INDEXING
# --------------------------------

numbers = [10, 20, 30, 40]

print("\nList Indexing:")
print(numbers[0])   # 10
print(numbers[-1])  # 40

# --------------------------------
# TUPLE INDEXING
# --------------------------------

t = (1, 2, 3, 4)

print("\nTuple Indexing:")
print(t[2])   # 3
print(t[-1])  # 4

# --------------------------------
# SLICING (ADVANCED INDEXING)
# --------------------------------

print("\nSlicing Examples:")
print(text[0:4])   # Pyth
print(text[:3])    # Pyt
print(text[2:])    # thon
print(text[-4:-1]) # tho

# --------------------------------
# STEP IN SLICING
# --------------------------------

print("\nSlicing with Step:")
print(text[::2])   # Pto
print(text[::-1])  # nohtyP (reverse)

# --------------------------------
# IMPORTANT RULES
# --------------------------------

# Index Out of Range (Uncomment to see error)
# print(text[10])   # ERROR

# Strings are Immutable
# text[0] = "H"   # ERROR

# --------------------------------
# PRACTICE
# --------------------------------

data = "Programming"

print("\nPractice:")
print(data[0])      # First character
print(data[-1])     # Last character
print(data[3:7])    # Substring
print(data[::-1])   # Reverse

# --------------------------------
# END OF NOTES
# --------------------------------