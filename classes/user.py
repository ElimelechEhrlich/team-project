from uuid import uuid4

class User:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.borrowed_books:list = []
    
    def __str__(self):
        return f"name: {self.name}, id: {self.id}"