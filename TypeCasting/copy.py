# Copy in Python

import copy

# --------------------------------
# 1. GENERAL COPY (Assignment)
# --------------------------------
# Both variables refer to SAME object

a = [1, 2, 3]
b = a

b[0] = 100

print("General Copy:")
print(a)  # [100, 2, 3]
print(b)  # [100, 2, 3]

# --------------------------------
# 2. SHALLOW COPY
# --------------------------------
# Creates new object but inner objects are shared

a = [[1, 2], [3, 4]]
b = a.copy()   # or copy.copy(a)

b[0][0] = 100

print("\nShallow Copy:")
print(a)  # [[100, 2], [3, 4]]
print(b)  # [[100, 2], [3, 4]]

# Outer list is different, inner lists are same

# --------------------------------
# 3. DEEP COPY
# --------------------------------
# Creates completely independent copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print("\nDeep Copy:")
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[100, 2], [3, 4]]

# --------------------------------
# IMPORTANT NOTES
# --------------------------------

# General Copy → same memory
# Shallow Copy → new outer, same inner
# Deep Copy → fully independent