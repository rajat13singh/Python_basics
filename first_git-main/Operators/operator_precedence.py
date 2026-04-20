# Operator Precedence in Python
# Determines which operation is performed first

# Order (highest to lowest):
# 1. ** (Exponent)
# 2. *, /, //, %
# 3. +, -
# 4. Relational (>, <, >=, <=, ==, !=)
# 5. not
# 6. and
# 7. or

# Example 1
result = 2 + 3 * 4
print(result)   # 14 (3*4 first, then +)

# Example 2
result = (2 + 3) * 4
print(result)   # 20 (brackets first)

# Example 3
result = 2 ** 3 * 2
print(result)   # 16 (2**3 = 8, then *2)

# Example 4
result = 10 / 2 + 3
print(result)   # 8.0 (10/2 first, then +)

# Example 5 (Relational)
print(5 > 3 and 2 < 1)   # False

# Example 6 (not, and, or)
print(not True or False)   # False
# not True → False, then False or False → False

# Important notes
# () has highest priority → always solved first
# Follow BODMAS rule
# Use brackets to avoid confusion