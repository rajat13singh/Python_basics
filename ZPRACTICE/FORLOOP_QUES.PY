#ACCEPT AN INTEGER AND PRINT HELLO WORLD N TIMES
n=int(input("enter the value:-"))
for i in range(n):
    print("hello world")
#PRINT NATURAL NUMBERS UPTO N
for i in range(1,n+1):
    print(i)
#REVERSE FOR LOOP ,PRINT N TO 1
for i in range(n,0,-1):
    print(i)
#print table of n
for i in range(n,n*10+1,n):
    print(i)
#sum of n terms
sum=0  #its like a empth box in which i wil stores one by one and at the end we will recieve our expected output
for i in range(1,n+1):
    sum=sum+i
print(sum)
#factorial of a numbr
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(fact)
#print sum of even numbers seperatly
sum_even=0
for i in range(2,n+1,2):
    sum_even=sum_even+i
print(sum_even)
#print sum of odd numbers seperatly
sum_odd=0
for i in range(1,n+1,2):
    sum_odd=sum_odd+i
print(sum_odd)
#find the factors of the numbr
#factors will fully devide  the number i.e remainder will be zero
x=int(input("enter the digit whose factors you want>>>>>>"))
for i in range(1,x+1):
    if x%i==0:
        print(i)
#accept a number and check whether its perfect number or not 
#a number whose sum of fsctors are equal to the number itself but dont include the number itsself
sum_i=0
for i in range(1,x):
    if x%i==0:
        sum_i+=i
if sum_i==x:
    print("its the perfect number")
else:
    print("its not perfect")    
#check whether the number is prime or not


