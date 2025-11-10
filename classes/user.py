from uuid import uuid4
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = uuid4()
        self.borrowed_books = []

    