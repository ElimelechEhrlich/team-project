class Menu:
    def __init__(self):
        pass

    def show_menu(self):
        print("1. Add a book \n2. Add a new user \n3. Borrow  a book \n4. Return a book \n5. Show all availble books \n6. Search for a book or author \n7. Save&Exit")
        print()
    
    def user_input(self):
        self.show_menu(self)
        user = input("• Please entering your choice: ")
        return user