from uuid import uuid4
class Book:
    def __init__(self,title: str, author: str):
        self.title = title
        self.author = author
        self.ISBN = str(uuid4())
        self.is_available:bool = True

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, is_available:{self.is_available}"
    
