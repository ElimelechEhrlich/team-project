from uuid import uuid4
class Book:
    def __init__(self,title: str, auther: str):
        self.title = title
        self.authr = auther
        self.ISBN:int = uuid4()
        self.is_available:bool = True

    def __str__(self):
        return f"title: {self.title}, auther: {self.authr}, is_avilable:{self.is_available}"
    
