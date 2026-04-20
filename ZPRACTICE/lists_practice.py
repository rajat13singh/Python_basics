#the major difference between the list ,tuple and string is list is mutable as it value can be changed
#print positive and negative elements from the list
L=[1,2,4,-5,6,-44,-102]
print("positive numbers are:>>>")
for i in L:
    if (i>=0):
        print(i)
print("negative elemets are:>>>>>")        
for i in L:
    if i<=0:
        print(i)   
#mean of list elements
sum=0 
for i in L:
    sum=sum+i
print(sum)
print(sum/len(L))
#find the gratest from the list and write its index too
largest=L[0]
index=0 
for i in range(len(L)):
    if L[i]>largest:
        largest=L[i]
        index=i
print(f"largest is {largest}")
#for second largest
second_largest=L[0]
for i in range(len(L)):
    if second_largest<L[i]<largest:
        second_largest=L[i]
        index=i
print(f"second largest is {second_largest}")   
index1=L[largest]  
print(index1)


      


        
        

    