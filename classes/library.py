from class_Book import Book
from user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book:Book):
        self.list_of_books.append(book)

    def add_user(self, user:User):
        self.list_of_users.append(user)

    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if book.is_avalable == False:
                    return 'book is not available!'
                else:
                    for user in self.list_of_users:
                        if user.id == user_id:
                            user.borrowed_books.append(book)
                            book.is_avalable == False
                            book.found_by_user = user_id
                            return
                        else:
                            continue
                    return 'user not registered in the library.'      
            return 'book is not exist!'
            
    def return_book(self, user_id, book_isbn):
        for user in self.list_of_users:
            if user.id == user_id:
                for book in user.borrowed_books:
                    if book.ISBN == book_isbn:
                        book.is_avalable == True
                        book.found_by_user = None
                        user.borrowed_books.pop(book)
                        return
                return 'book is not in borrowed_books list of user'
        return 'user not registered in the library.'




     