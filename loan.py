class Loan :
    def __init__(self, loan_id, member_id, book_id, loan_date, return_date = None):
        self.loan_id = loan_id
        self.member_id = member_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def display_info(self):
        print("\n--- Loan Details ---")
        print(f"Loan ID: {self.loan_id}")
        print(f"Member ID: {self.member_id}")
        print(f"Book ID: {self.book_id}")
        print(f"Loan Date: {self.loan_date}")
        if self.return_date:
            print (f"Return Date: {self.return_date}")
        else:
            print(f"Return Date: Not Returned") 

    def mark_returned(self, return_date):
        self.return_date = return_date

    def is_active(self):
        return self.return_date is None    