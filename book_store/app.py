import utility.database as db

user_choices = "\nEnter 'a' to add a book,\nEnter 'l' to list all the books,\nEnter 'd' to delete a book,\nEnter 'r' to mark a book as read,\nEnter 'q' to quit\n:"
def menu():
    db.create_book_table()
    user_input = input(user_choices)
    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'd':
            delete_book()
        elif user_input == 'r':
            mark_book_as_read()
        else:
            print("Unknown command.Try again...")
        user_input = input(user_choices)

def add_book():
    name = input("Enter book name to store : ")
    author = input("Enter the name of the author : ")
    status = int(input("Have you read the book? (0 for no | 1 for yes) : "))
    db.add_book_to_database(name, author, status)
    print("Book inserted")

def list_books():
    books = db.get_all_books()
    for book in books:
        read = "YES" if book['read'] == 1 else "NO"
        print(f"{book['name']} by {book['author']}, read:{read}")

def mark_book_as_read():
    name = input("Enter the name of the book to mark as read : ")
    db.mark_as_read(name)

def delete_book():
    name = input("Enter the name of the book to delete : ")
    db.remove_book(name)

menu()
