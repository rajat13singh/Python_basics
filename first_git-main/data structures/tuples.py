#tuples is most secure datatype as it is not MUTABLE
# What is a Tuple?
# -----------------------------
# A tuple is a collection of elements similar to a list.
# Tuples are ORDERED but IMMUTABLE (cannot be changed).
# Tuples allow duplicate values.
#we cant assign values to tuple index as its immutable
#there should be in one single comma if we are using single value tuple otherwise it will be int type
numbers = (1, 2, 3, 4)

print(numbers)



# -----------------------------
# Creating Tuples
# -----------------------------
# Using parentheses

tuple1 = (10, 20, 30)

print(tuple1)


# Tuple with different datatypes

mixed_tuple = (1, "apple", 3.14, True)

print(mixed_tuple)


# Creating tuple using tuple() function

tuple2 = tuple([5, 6, 7])

print(tuple2)



# -----------------------------
# Single Element Tuple
# -----------------------------
# To create a single element tuple, a comma is required.

single = (5,)   # correct

print(single)



# -----------------------------
# Accessing Tuple Elements
# -----------------------------
# Tuples use indexing like lists.

numbers = (10, 20, 30, 40)

print(numbers[0])   # first element
print(numbers[2])   # third element



# -----------------------------
# Tuple Slicing
# -----------------------------
# Slicing allows accessing a range of elements.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])   # elements from index 1 to 3



# -----------------------------
# Tuple Length
# -----------------------------
# len() returns the number of elements in the tuple.

numbers = (1, 2, 3, 4)

print(len(numbers))



# -----------------------------
# count()
# -----------------------------
# count() returns how many times a value appears.

numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))



# -----------------------------
# index()
# -----------------------------
# index() returns the position of the first occurrence.

numbers = (10, 20, 30)

print(numbers.index(20))



# -----------------------------
# Tuple Packing
# -----------------------------
# Assigning multiple values to a tuple.

tuple1 = 1, 2, 3

print(tuple1)



# -----------------------------
# Tuple Unpacking
# -----------------------------
# Extracting values from a tuple into variables.

tuple1 = (10, 20, 30)

a, b, c = tuple1

print(a)
print(b)
print(c)



# -----------------------------
# Converting Tuple to List
# -----------------------------
# Since tuples are immutable, convert to list to modify.

numbers = (1, 2, 3)

numbers_list = list(numbers)

numbers_list.append(4)

print(numbers_list)



# -----------------------------
# Important Properties of Tuples
# -----------------------------
# 1. Tuples are ordered
# 2. Tuples allow duplicate elements
# 3. Tuples are immutable (cannot be changed)
# 4. Tuples are faster than lists
# 5. Used when data should not change