class Book:
    def __init__(self,title: str, auther: str, ISBN:int):
        self.title = title
        self.authr = auther
        self.ISBN = ISBN
        self.is_availble = True

    def __str__(self):
        return f"title: {self.title}, auther: {self.authr}, is_avilable:{self.is_availble}"
    
