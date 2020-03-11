import sqlite3 as sq
from datetime import datetime, date

con = sq.connect("novel.db")
c = con.cursor()

def get_novels(): #retrieving data from table
    res = c.execute("SELECT Title, AuthorName FROM Novel JOIN Author \
                    WHERE Novel.AuthorID = Author.AuthorID")
    data = c.fetchall() 
    return data

def get_authors(): #retrieving data from table
    res = c.execute("SELECT AuthorName FROM Author")
    data = c.fetchall() 
    return data

def add_to_database(title, book_id, dt, author_id): #adding novel to database
    ins_str = 'INSERT INTO Novel (Title, BookID, NovelPD, AuthorID) \
    Values ("' + str(title) + '", ' + str(book_id) + ', "\
    ' + str(dt) + '", ' + str(author_id) + ');'
    res = c.execute(ins_str)
    con.commit()		


def render_menu(): #main menu
    print("1. Display Novels")
    print("2. Add Novel")
    print("3. Quit")
    choice = input("\nChoose an option:\t")

    #check for valid input
    while choice not in ("1", "2", "3"):
        print("Invalid")
        choice = input("Choose an option:\t")
    choice = int(choice)
    
    if choice == 1:
        display_novels()
    elif choice == 2:
        add_novel()
    elif choice == 3:
        end_program()
        return False;
    return True;
    
def end_program(): #option number 3
    print("End Program")
    con.close()

def display_novels(): #option number 1
    novels = get_novels()
    tbl = "-" * 60 + "\n"
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += " " * (40 - len(field))
        tbl += "\n"
    tbl += "-" * 60
    print("\n" + "Title" + " " * 35 + "Author")
    print(tbl)

def add_novel(): #option number 2
    print("\n")

    #gettin AuthorID
    author_name = get_authors()
    num_authors = 1
    for row in author_name:
        for field in row:
            print(str(num_authors) + ": " + str(field))
            num_authors = num_authors + 1
    author_id = input("\nChoose an author: ")
    #check for valid author choice
    while author_id not in ("1", "2", "3", "4"):
        print("Invalid")
        author_id = input("Choose an author: ")
    author_id = int(author_id)

    #getting Title
    title = input("Title of book: ")

    #getting NovelPD (publication date)
    day = input("Day of publication date: ")
    month = input("Month of publication date: ")
    year = input("Year of publication date: ")

    #getting BookID
    novels = get_novels()
    num_books = 0
    for row in novels:
        num_books = num_books + 1
    book_id = num_books + 1
    
    check_and_enter_selection(title, book_id, day, month, year, author_id)


def check_and_enter_selection(title, book_id, day, month, year, author_id):
    try:
        dt = date(int(year), int(month) , int(day))
        add_to_database(title, book_id, dt, author_id)
        print("\nSuccess", "Your novel has been added")
    except:
        print("Invalid Date")

while(render_menu()):
    print("\n")



