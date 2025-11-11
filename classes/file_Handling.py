import json


class FileHandling:
    def __init__(self):
        pass

    def write_books(self, books:list):
        with open('books_data.json', 'w') as bd:
            books_dict = []
            for book in books:
                books_dict.append(book.__dict__)
            books_json_type = json.dumps(books_dict, indent=2)
            bd.write(books_json_type)

    def read_books(self):
        with open('books_data.json', 'r') as bd:
            books_data = bd.read()
            books_py_type = json.loads(books_data)
            # reading_books_file = bd.read(books_py_type)
            return books_py_type

    def write_users(self, users:list):
        with open('users_data.json', 'w') as ud:
            users_dict = []
            for user in users:
                users_dict.append(user.__dict__)
            users_json_type = json.dumps(users_dict, indent=2)
            ud.write(users_json_type)

    def read_users(self):
        with open('users_data.json', 'r') as ud:
            users__data = ud.read()
            users_py_type = json.loads(users__data)
        #   users__data = ud.read(users_py_type)
            return users_py_type
