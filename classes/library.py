from class_Book import Book
from user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def return_list_of_books(self):
        return self.list_of_books

    def add_book(self, book:Book):
        self.list_of_books.append(book)

    def add_user(self, user:User):
        self.list_of_users.append(user)

    def list_availble_books(self):
        list_availble_books = []
        for book in self.list_of_books:
            if book.is_availble == True:
                list_availble_books.append(book)
                return list_availble_books
   
class SearchBook:
    def __init__(self):
        self.books_list = Library.return_list_of_books()

            
