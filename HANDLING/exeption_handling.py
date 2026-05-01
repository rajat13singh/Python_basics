#there are many errors ex- syntax error ,indentqtion errror these are the errors which are not handled if you done this wrong
#and except these errors all errors can be handled
#ZERO DIVISION ERROR
#in this if the division is done by dividing zero which is done by the useer input there is no error in syntax
#a=int(input("enter the value of a:-"))
#print(10/a) #if someone give the value of a =0
#print("hello world") #now this will not be print as the previous live gives an error that disrupts the flow of the code
#so basically the exceptions are unexpected events or errors thst occurs during the execution of a program whcih disrupts the normal flow of the program

#try and except


a=int(input("enter the value of a:-"))
try:
    print(10/a)
except Exception as err: #for all type of error write except Exception as err:
    print(f"sorry you cannot divide it by {a}")
print("this is how try and except works.....")   

#else
b=int(input("enter the value of b:-"))
try:
    print(10/b)
except Exception as err: #for all type of error write except Exception as err:
    print(f"sorry you cannot divide it by {b}")
else: #this will work when except dont have any work
    print("this is how else works")    
print("this is how try and except works.....")  


#finally

#it will print whether thers error or not
c=int(input("enter the value of c:-"))
try:
    print(10/c)
except Exception as err: #for all type of error write except Exception as err:
    print(f"sorry you cannot divide it by {c}")
else: #this will work when except dont have any work
    print("this is how else works")    
finally:
    print("i will run no matter except run or not")    
print("this is how try and except works.....")  


#raise 

# it will throw exception manually
age=int(input("tell your age:-"))
try:
    if age<10 or age>18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("welcome to the club")
        print("the club will start soon")
except Exception as err:
    print(f"an error occured as {err}")








