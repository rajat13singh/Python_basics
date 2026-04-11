#the block of resusable code is knows=n as codes ,it helps to looks better and also esy
#there are tree parameters :- definition ,declaration,function call
#greetings:-
def greet(name,age,gender):
    if gender=='male':
        print(f"hello {name} sir,how are you ,so your age is {age},nice")
    elif gender=='female': 
        print(f"hello {name} mam,how are you ,so your age is {age},nice") 
name=input("enter your name:-")
age=int(input("enter your age:-"))
gender=input("whats your gender (male/female):-")
greetings=greet(name,age,gender)
    