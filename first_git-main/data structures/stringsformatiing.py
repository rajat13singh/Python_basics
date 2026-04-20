#normal formatting
a=10
b=13
sum=a+b
print("sum is {}".format(sum))#this is called placeholders {}
print("sum is {}".format("100"))
print("sum is {} and {} and {}".format("10","23","122")) #multiple placeholders
#index based formatting
print("sum is {2} and {1} and {0}".format("66","44","12"))
#value based formattting
print("values of {a},{b}".format(a=22,b=55))
##>>>>>>F STRINGS<<<<<<<<<##
print(f" the sum of {a},{b} is {sum}")