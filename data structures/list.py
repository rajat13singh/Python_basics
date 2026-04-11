#list are mutable(can be changed)
a=[12,23,34,14]
#list are duplicable(can be multiple duplicate value)
b=[12,13,12]
#ordered(they values got there index values)
#heterogenous(we can have multiple data types inside the list)
c=[12,13,14,"string",4.8,print()]
print(c[3])
#loops with lists
for i in range(len(a)):
    print(a[i])
help(list)    
# METHODS LISTS
# 1. append()
# -----------------------------
# append() adds ONE element to the end of the list.

numbers = [1, 2, 3]

numbers.append(4)   # adds 4 at the end

print(numbers)      # Output: [1, 2, 3, 4]


# -----------------------------
# 2. extend()
# -----------------------------
# extend() adds multiple elements from another list
# to the current list.

numbers = [1, 2, 3]

numbers.extend([4, 5, 6])   # adds all elements

print(numbers)              # Output: [1, 2, 3, 4, 5, 6]


# -----------------------------
# 3. insert()
# -----------------------------
# insert(index, element)
# inserts an element at a specific position.

numbers = [1, 2, 3]

numbers.insert(1, 10)   # insert 10 at index 1

print(numbers)          # Output: [1, 10, 2, 3]


# -----------------------------
# 4. remove()
# -----------------------------
# remove(value)
# removes the FIRST occurrence of the value.

numbers = [1, 2, 3, 2]

numbers.remove(2)   # removes first 2

print(numbers)      # Output: [1, 3, 2]


# -----------------------------
# 5. pop()
# -----------------------------
# pop() removes and returns element by index.
# If no index given, removes the last element.

numbers = [1, 2, 3, 4]

numbers.pop()       # removes last element

print(numbers)      # Output: [1, 2, 3]

numbers.pop(1)      # removes element at index 1

print(numbers)      # Output: [1, 3]


# -----------------------------
# 6. clear()
# -----------------------------
# clear() removes ALL elements from the list.

numbers = [1, 2, 3]

numbers.clear()

print(numbers)      # Output: []


# -----------------------------
# 7. index()
# -----------------------------
# index(value)
# returns the index position of the first occurrence.

numbers = [10, 20, 30]

print(numbers.index(20))   # Output: 1


# -----------------------------
# 8. count()
# -----------------------------
# count(value)
# counts how many times an element appears.

numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))    # Output: 3


# -----------------------------
# 9. sort()
# -----------------------------
# sort() arranges the list in ascending order.

numbers = [5, 1, 4, 2]

numbers.sort()

print(numbers)    # Output: [1, 2, 4, 5]


# sort(reverse=True) sorts in descending order.

numbers.sort(reverse=True)

print(numbers)    # Output: [5, 4, 2, 1]


# -----------------------------
# 10. reverse()
# -----------------------------
# reverse() reverses the order of elements.

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)    # Output: [4, 3, 2, 1]


# -----------------------------
# 11. copy()
# -----------------------------
# copy() creates a shallow copy of the list.

numbers = [1, 2, 3]

new_list = numbers.copy()

print(new_list)   # Output: [1, 2, 3]