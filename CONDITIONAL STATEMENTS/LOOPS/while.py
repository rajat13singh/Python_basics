# for loop
for i in range(5):
    print(i)

# for with start, stop, step
for i in range(1, 10, 2):
    print(i)

# loop through list
nums = [10, 20, 30]
for n in nums:
    print(n)

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

# nested for
for i in range(3):
    for j in range(2):
        print(i, j)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# while with break
i = 0
while True:
    if i == 3:
        break
    print(i)
    i += 1

# while with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# while else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("done")

# infinite loop (example)
# while True:
#     print("running")

# sum using while
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total)