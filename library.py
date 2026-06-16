from datetime import date
from loan import Loan

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print(f"Book with ID {book.book_id} already exists.")
                return

        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print(f"Member with ID {member.member_id} already exists.")
                return
       
        self.members.append(member)
        print("Member added successfully")

    def create_loan(self, loan):
        self.loans.append(loan)
    
    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_info() 

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.display_info()
                return book
            
        print (f"Book with this ID {book_id} does not exist.")
        return None 
                
    def search_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                member.display_info()
                return member
            
        print (f"Member with this ID {member_id} does not exist.")
        return None
    
    def search_active_loan(self, member_id, book_id):
        for loan in self.loans:
            if loan.member_id == member_id and loan.book_id == book_id and loan.is_active():
                return loan
        print (f"No active loan found for Member ID {member_id} and Book ID {book_id}.")
        return None
    
    def borrow_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)
        if member is None:
            return
        if book is None:
            return
        
        if not book.is_available:
            print("Book is not available for borrowing.")
            return
        
        loan_id = f"L{len(self.loans) + 1:03d}"
        loan_date = str(date.today())
        loan = Loan(loan_id, member_id, book_id, loan_date)
        self.create_loan(loan)  
        book.borrow_book()
        member.borrow_book(book_id)
        print(f"Loan {loan_id} created successfully.")

    def return_book(self, member_id, book_id):
        member = self.search_member(member_id)
        book = self.search_book(book_id)
        
        if member is None:
            return
        if book is None:
            return
        
        loan = self.search_active_loan(member_id, book_id)
        
        if loan is None:
            return
        
        loan.mark_returned(str(date.today()))
        book.return_book()
        if book_id in member.borrowed_books:
            member.return_book(book_id)
        print(f"Loan {loan.loan_id} marked as returned.")
    
    def display_members(self):
        print("\n--- Library Members ---")
        
        for member in self.members:
            member.display_info()

    def display_loans(self):
        print("\n--- Library Loans ---")
        for loan in self.loans:
            loan.display_info()

    def generate_book_id(self):
        return f"B{len(self.books) + 1:03d}"

    def generate_member_id(self):
        return f"M{len(self.members) + 1:03d}"
    