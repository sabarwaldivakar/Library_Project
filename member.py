class Member:
    """Represents a library member and their borrowed books."""
    
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def display_info(self):
        print("\n--- Member Details ---")
        print(f"ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print("\nBorrowed Books:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print("No books borrowed.")

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            print("Book not found in borrowed list.")

    def view_borrowed_books (self):
        if self.borrowed_books:
            print("\nBorrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:  
            print("No books borrowed.")

