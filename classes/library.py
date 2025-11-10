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

     