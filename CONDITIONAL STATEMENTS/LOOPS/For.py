# basic for loop
for i in range(5):
    print(i)

# range with start, stop
for i in range(1, 6):
    print(i)

# range with step
for i in range(1, 10, 2):
    print(i)

# loop through list
nums = [10, 20, 30]
for n in nums:
    print(n)

# loop through string
for ch in "python":
    print(ch)

# using len
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    print(arr[i])

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# else with for
for i in range(3):
    print(i)
else:
    print("done")

# nested for loop
for i in range(3):
    for j in range(2):
        print(i, j)

# pattern example
for i in range(5):
    print("*" * (i + 1))

# sum of numbers
total = 0
for i in range(1, 6):
    total += i
print(total)

# iterate dictionary
d = {"a": 1, "b": 2}
for key in d:
    print(key, d[key])

# using items()
for key, value in d.items():
    print(key, value)