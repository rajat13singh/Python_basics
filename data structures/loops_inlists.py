num=[1,2,3,10,4]
for val in num:
    print(val) #ek ek krke value variable ke andar list ke elements aa jayege
x=10
idx=0
for val in num:
    if(val==x):
        print(idx)
        break
    idx+=1  #this whole process is called linear search as we checking one by one by going to paricular index
    