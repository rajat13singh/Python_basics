#ask a user to enter string and check the palindrome
string1=input("enter the word here:")
if string1==string1[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")
#print average of the integers present in the list
list=[12,23,4,5,5,66]
sum=0 
for i in list:
    sum=sum+i
    i=0
print(f"so average of the elements in the list is {sum/len(list)}")
#ask user to enter the elements to the two lists and combine them in one and after that sort it 
# This merges, then sorts, then prints
print(sorted(eval(input("List 1: ")) + eval(input("List 2: "))))