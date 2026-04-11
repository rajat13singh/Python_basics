# Print positive and negative elements of an List.
# Find the greatest element and print its index too.
# Find the second greatest element.
# Check if List is sorted or not.
#-----------------------------------------
a=[12,14,-4,-6,0,-44,77]
for i in range(len(a)): #this is with the the indexing 
    if (a[i]>0):
        print(a[i])
    elif (a[i]<0):
        print(a[i])   
#without indexing
print("the positive numbers are :-")
for i in a:
    if(i>=0):
        print(i)
print("the negative numbers are:-")
for i in a:
    if(i<=0):
        print(i)
# Mean of List elements.
b=[2,4,3,5,6]
