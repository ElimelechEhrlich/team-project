from classes.class_Book import Book
from classes.user import User
from classes.library import Library
from classes.iu import Menu

library1 = Library()
book1 = Book('A Little Book for Little Children', 'Thomas White')
book2 = Book('A Token for Children', 'James Janeway')
book3 = Book('Divine Songs', 'Isaac Watts')
book4 = Book('A Description of Three Hundred Animals', 'Thomas Boreman')
book5 = Book('The Gigantick History of the Two Famous Giants', 'Thomas Boreman')
book6 = Book('Winter-Evening Entertainments', 'Nathaniel Crouch')
book7 = Book('The History of Fortunatus', 'Thomas Churchyard')
user1 = User('elimelch ehrlich')
books = [book1,book2,book3,book4,book5,book6,book7]
for book in books:
    library1.add_book(book)
library1.add_user(user1)

if __name__=='__main__':
    
        
        choice = None
        while choice != "7":
            choice = Menu.user_input(Menu)
            if choice == "1":
                book_title = str(input('title: '))
                book_author = str(input('author: '))
                book = Book(book_title, book_author)
                library1.add_book(book)
            elif choice == "2":
                user_name = str(input('name: '))
                user = Book(user_name)
                library1.add_user(user)
            elif choice == "3":
                user_id = input('user_id: ')
                book_id = input('book_id: ')
                library1.borrow_book(user_id, book_id)
            elif choice == "4":
                user_id = input('user_id: ')
                book_id = input('book_id: ')
                library1.return_book(user_id, book_id)
            elif choice == "5":
                library1.list_availble_books()
            elif choice == "6":
                user_input = input('add title or author: ')
                library1.search_book(user_input)
            elif choice == "7":
                library1.file_Handling()
            else:
                print("Invalid choice, try again.")







