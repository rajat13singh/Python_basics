# What is a Dictionary?
# -----------------------------
# A dictionary stores data in KEY : VALUE pairs.
# Dictionaries are unordered, mutable, and indexed by keys.
#defaultly dictionary is empty

student = {
    "name": "Rajat",
    "age": 20,
    "course": "Python"
}

print(student)



# -----------------------------
# Accessing Values
# -----------------------------
# Values can be accessed using their keys.

student = {
    "name": "Rajat",
    "age": 20
}

print(student["name"])   # Output: Rajat
print(student["age"])    # Output: 20



# -----------------------------
# Using get()
# -----------------------------
# get() returns the value of a key.
# If the key does not exist, it does NOT give an error.

student = {
    "name": "Rajat",
    "age": 20
}

print(student.get("name"))



# -----------------------------
# Adding or Updating Values
# -----------------------------
# New key-value pairs can be added or existing ones updated.

student = {
    "name": "Rajat",
    "age": 20
}

student["age"] = 21      # updating value
student["city"] = "Delhi"  # adding new key-value pair

print(student)



# -----------------------------
# Removing Elements
# -----------------------------
# pop() removes an element using its key.

student = {
    "name": "Rajat",
    "age": 20
}

student.pop("age")

print(student)



# -----------------------------
# popitem()
# -----------------------------
# popitem() removes the last inserted key-value pair.

student = {
    "name": "Rajat",
    "age": 20,
    "city": "Delhi"
}

student.popitem()

print(student)



# -----------------------------
# clear()
# -----------------------------
# clear() removes all elements from the dictionary.

student = {
    "name": "Rajat",
    "age": 20
}

student.clear()

print(student)



# -----------------------------
# keys()
# -----------------------------
# keys() returns all the keys in the dictionary.

student = {
    "name": "Rajat",
    "age": 20,
    "city": "Delhi"
}

print(student.keys())



# -----------------------------
# values()
# -----------------------------
# values() returns all values.

print(student.values())



# -----------------------------
# items()
# -----------------------------
# items() returns key-value pairs as tuples.

print(student.items())



# -----------------------------
# update()
# -----------------------------
# update() adds multiple key-value pairs.

student = {
    "name": "Rajat",
    "age": 20
}

student.update({"city": "Delhi", "course": "Python"})

print(student)



# -----------------------------
# Looping Through Dictionary
# -----------------------------
# Looping through keys and values.

student = {
    "name": "Rajat",
    "age": 20,
    "city": "Delhi"
}

for key, value in student.items():
    print(key, ":", value)



# -----------------------------
# Important Properties of Dictionary
# -----------------------------
# 1. Data stored as key : value pairs
# 2. Keys must be unique
# 3. Values can be duplicated
# 4. Dictionaries are mutable
# 5. Keys must be immutable (string, number, tuple)