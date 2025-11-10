from class_Book import Book
from user import User
from library import Library
from iu import Menu


if __name__ == '__nain__':
    library = Library()
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
        library.add_book(book)
    library.add_user(user1)

    print(library.list_availble_books())

