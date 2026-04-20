#write a program to print the length of the list
a=[12,34,56,77,34]
def length(x):
    length=len(a)
    print(f"so the length of the list is {length}")
length(a)
#write a program to print the elemts of the list in a single line
b=[12,34,56,77,34]
def elements(x):
    for i in range(len(b)):
        print(b[i],end=" ")
elements(b)
#write a function to find the factorial of n
def fact(k):
    fact=1
    for i in range(1,k+1):
        fact=fact*i
    print(fact)
x=int(input("\nenter the value of x:-"))
fact(x)        
#waf to convert usd into inr
def currency_dollar(y):
    currency_rupees=y*95
    print(currency_rupees)
z=int(input("\nenter the currency in dollar:-"))
currency_dollar(z)    
#if a input is even print even and if the function is oddd print odd
def userinput(i):
    if i%2==0:
        print("EVEN")
    else:
        print("ODD") 
n=int(input("enter the value of n:-"))
userinput(n)           