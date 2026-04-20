# ==========================================
# PYTHON SLICING COMPLETE NOTES
# ==========================================

# 🔹 What is Slicing?
# Slicing means extracting a part (substring/sublist) from a sequence
# Syntax: sequence[start : end : step]

# ------------------------------------------
# BASIC STRING SLICING
# ------------------------------------------

text = "Python"

print("Original String:", text)

# start : end (end is excluded)
print("\nBasic Slicing:")
print(text[0:4])   # Pyth
print(text[1:5])   # ytho

# ------------------------------------------
# DEFAULT VALUES
# ------------------------------------------

print("\nDefault Slicing:")
print(text[:4])    # start = 0 → Pyth
print(text[2:])    # end = last → thon
print(text[:])     # full string → Python

# ------------------------------------------
# NEGATIVE SLICING
# ------------------------------------------

print("\nNegative Slicing:")
print(text[-4:-1])  # tho
print(text[-6:-3])  # Pyt

# ------------------------------------------
# STEP IN SLICING
# ------------------------------------------

print("\nSlicing with Step:")
print(text[::2])    # Pto (skip 1)
print(text[1::2])   # yhn
print(text[::-1])   # nohtyP (reverse)

# ------------------------------------------
# EXAMPLE WITH "rajnish"
# ------------------------------------------

name = "rajnish"

print("\nExample (rajnish):")
print(name[3:7])   # nish

# Index positions:
# r a j n i s h
# 0 1 2 3 4 5 6

# ------------------------------------------
# LIST SLICING
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("\nList Slicing:")
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]

# ------------------------------------------
# TUPLE SLICING
# ------------------------------------------

t = (1, 2, 3, 4, 5)

print("\nTuple Slicing:")
print(t[2:5])   # (3, 4, 5)

# ------------------------------------------
# IMPORTANT RULES
# ------------------------------------------

# 1. End index is NOT included
print("\nRule Check:")
print(text[0:2])   # Py (not Pyt)

# 2. Step cannot be zero
# print(text[::0])  # ERROR

# 3. Works on strings, lists, tuples

# ------------------------------------------
# PRACTICE
# ------------------------------------------

data = "Programming"

print("\nPractice:")
print(data[0:6])   # Progra
print(data[-5:])   # mming
print(data[::-1])  # reverse

# ==========================================
# END OF NOTES
# ==========================================
name="RAJNISH"
print(name[3:7])
print(name[-4:])
print(name[0:1])
print(name[-4::-1])