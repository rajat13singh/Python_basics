#any name with the etension ex .py,.txt,.mp3 etc arerr the file
#and to handle these extensions are called file handling

#file Handling:- creating,reading,updating,deleting  (CRUD) operations that we can perform in files
#we have to use open() to open a file in python
p=open(r'D:\AIML\capegemini_projects\Game\main.py')
print(p.read())
#there are the multiple modes to open the ffile
#'r':-read-"files must exist"
#'w':- write -"creates file or overwrites"
#'a':- append-"adds to end of file"
#'x':- create :- creates a new file,fails if it exits
r=open("superman.txt",'w') #this will create the file if dont exist
r.write("Hello this is rajat and i am writing inside this file ")#this will write inside that file without even opening that file
r.close()#closing file is important otherwise it will open always
r=open("superman.txt",'a') #for adding to the file
r.write("now i am  appending this content to that that file")
r.close() #this means a also creates and add /write the content 
#but x only creates it doesnt write or read
