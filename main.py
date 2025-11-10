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

if __name__=='__main__':


    library1.add_user(user1)
    print(book1.title)
    print(library1.list_of_books)
    print(library1.list_availble_books())

