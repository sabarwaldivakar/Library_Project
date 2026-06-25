class Book :
    """Represents a book with details and borrowing status."""

    def __init__ (self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"

        print("\n--- Book Details ---")
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {status}")

    def borrow_book(self):
        if not self.is_available:
            print("Book is already borrowed.")
        else:
            self.is_available = False
            print("Book borrowed successfully.")

    def return_book(self):
        if self.is_available:
            print("Book is already available.")
        else:
            self.is_available = True
            print("Book returned successfully.")

    def update_book_details(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        print("Book details updated successfully.")


