from class_Book import Book
from user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self):
        self.list_of_books.append(Book())

    def add_user(self):
        self.list_of_users.append(User())

    