books = [
    "Atomic Habits",
    "The Alchemist",
    "Rich Dad Poor Dad",
    "Think and Grow Rich",
    "The Power of Your Subconscious Mind",
    "Ikigai",
    "Do Epic Shit", 
    "The Psychology of Money",
    "Deep Work",
    "The 7 Habits of Highly Effective People",
    "Can't Hurt Me",
    "Wings of Fire",
    "Harry Potter and the Philosopher’s Stone",
    "The Hobbit",
    "1984",
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "Sapiens: A Brief History of Humankind",
    "The Silent Patient",
    "The Subtle Art of Not Giving a F*ck"
]

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print(name,"is added")

def show_book():
    for b in books:
        print(b)
    print(">>>>>>>>>THESE ARE THE BOOKS AVAILABLE IN THE LIBRARY<<<<<<<<<<<")    

def issue_book():
    name = input("Enter book to issue: ")
    if name in books:
        books.remove(name)
        print(name,"is issued")
    else:
        print("book not found,sorry for inconvenience")

def return_book():
    name = input("Enter book to return: ")
    books.append(name)
    print(name,"returned successfully")

def library():
    while True:
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")

        choice = int(input("enter your choice:-"))

        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            break
        else:
            print("INVALID CHOICE,PLEASE CHOOSE BETWEEN 1 TO 5")

library()