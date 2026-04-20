# What is a Set?
# -----------------------------
# A set is a collection of UNIQUE elements.#NO DUPLICATES
# Sets are unordered (no fixed position/index).
# Duplicate values are automatically removed.
#semi heterogeneous

numbers = {1, 2, 3, 4}
print(numbers)



# -----------------------------
# Creating Sets
# -----------------------------
# Using curly brackets

set1 = {10, 20, 30}
print(set1)

# Using set() function

set2 = set([1, 2, 3, 4])
print(set2)



# -----------------------------
# Duplicate Elements Removed
# -----------------------------
# Sets automatically remove duplicates

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)    # Output: {1, 2, 3, 4}



# -----------------------------
# add()
# -----------------------------
# add() adds ONE element to the set.

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)



# -----------------------------
# update()
# -----------------------------
# update() adds MULTIPLE elements to a set.

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)



# -----------------------------
# remove()
# -----------------------------
# remove() deletes a specific element.
# It gives an error if the element does not exist.

numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)



# -----------------------------
# discard()
# -----------------------------
# discard() removes an element.
# It does NOT give an error if the element does not exist.

numbers = {1, 2, 3}

numbers.discard(5)

print(numbers)



# -----------------------------
# pop()
# -----------------------------
# pop() removes a RANDOM element from the set.

numbers = {10, 20, 30}

numbers.pop()

print(numbers)



# -----------------------------
# clear()
# -----------------------------
# clear() removes ALL elements from the set.

numbers = {1, 2, 3}

numbers.clear()

print(numbers)



# -----------------------------
# Union
# -----------------------------
# Combines two sets and removes duplicates.

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))



# -----------------------------
# Intersection
# -----------------------------
# Returns common elements in both sets.

A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))



# -----------------------------
# Difference
# -----------------------------
# Returns elements present in first set but not in second set.

A = {1, 2, 3}
B = {2, 3, 4}

print(A.difference(B))



# -----------------------------
# Important Properties of Sets
# -----------------------------
# 1. Sets are unordered
# 2. Sets do not allow duplicates
# 3. Sets are mutable (can be changed)
# 4. Elements inside sets must be immutable
#    (numbers, strings, tuples)