# STRING NOTES 
#strings is immutable
# creating strings
s = "hello world"

# indexing
print(s[0])      # h
print(s[-1])     # d

# slicing #ending index will not be printed
print(s[0:5])    # hello
print(s[::-1])   # reverse

# operations
a = "hello"
b = "world"
print(a + b)     # helloworld
print(a * 2)     # hellohello

# membership
print("he" in s)       # True
print("xyz" not in s)  # True

# functions
print(len(s))
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.count("l"))
print(s.find("o"))
print(s.replace("hello", "hi"))

# strip
s2 = "  hello  "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())

# split and join
s3 = "a,b,c"
print(s3.split(","))

l = ['a', 'b', 'c']
print(",".join(l))

# formatting
name = "Rajat"
age = 20
print(f"My name is {name} and age is {age}")

# immutability
s4 = "hello"
s4 = "H" + s4[1:]
print(s4)

# escape characters
print("hello\nworld")
print("hello\tworld")
print("He said \"Hi\"")

# type conversion
num = 10
s5 = str(num)
print(s5)

s6 = "123"
num2 = int(s6)
print(num2)