from classes.class_Book import Book
from classes.user import User
from classes.library import Library
from classes.iu import Menu
from classes.file_Handling import FileHandling

library1 = Library()
file_handling = FileHandling()
try:
    books = file_handling.read_books()
    users = file_handling.read_users()
except:
    pass

if __name__=='__main__':
        choice = None
        print(library1.list_of_books)
        print(library1.list_of_users)
        while choice != "7":
            choice = Menu.user_input(Menu)
            if choice == "1":
                book_title = str(input('title: '))
                book_author = str(input('author: '))
                book_id = int(input('book ISBN: '))
                book = Book(book_title, book_author, book_id)
                library1.add_book(book)
                for b in library1.list_of_books:
                    print(b.__dict__)
            elif choice == "2":
                user_name = str(input('name: '))
                user_id = int(input('user_id: '))
                user = User(user_name, user_id)
                library1.add_user(user)
                print(library1.list_of_users)
            elif choice == "3":
                print(library1.list_of_users[0])
                user_id = input('user_id: ')
                book_id = input('book_id: ')
                library1.borrow_book(user_id, book_id)
                print(library1.list_of_users[0])
            elif choice == "4":
                print(library1.list_of_users[0])
                user_id = input('user_id: ')
                book_id = input('book_id: ')
                library1.return_book(user_id, book_id)
                print(library1.list_of_users[0])
            elif choice == "5":
                print (library1.list_availble_books())
                print()
            elif choice == "6":
                user_input = input('add title or author: ')
                library1.search_book(user_input)
            elif choice == "7":
                file_handling.write_books(library1.list_of_books)
                file_handling.write_users(library1.list_of_users)
            else:
                print("Invalid choice, try again.")







