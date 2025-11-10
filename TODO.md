1. create basics classes: 
# Netanel Ozeri -  
Book:
    attributes: 
        title   
        author
        ISBN
        is_available (T/F)
    methods:
        repr() - prints book info
# Elimelech Ehrlich - Done
User:
    attributes:
        name
        id
        borrowed_books:list[books]
        
Library:
    attributes:
        list[books] = in a json file
        list[users] = in a json file
    methods:
        add_book(book)
        add_user(user)
        borrow_book(user_id, book_isbn)
        return_book(user_id, book_isbn)
        list_available_books()
        search_book(title or author)


