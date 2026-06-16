import csv
from book import Book
from member import Member
from loan import Loan
def save_books(books, filename="books.csv"):
    with open (filename, mode = "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Book ID", "Title", "Author", "Year", "Available"])

        for book in books:
            writer.writerow([book.book_id, book.title, book.author, book.year, book.is_available])


def save_members(members, filename="members.csv"):
    with open (filename, mode="w", newline="") as file:
        writer = csv.writer(file)
    
        writer.writerow(["Member ID", "Name", "Email"])

        for member in members:
            writer.writerow([member.member_id, member.name, member.email])

def save_loans(loans, filename="loans.csv"):
    with open (filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Loan ID", "Member ID", "Book ID", "Loan Date", "Return Date"])

        for loan in loans:
            writer.writerow([loan.loan_id, loan.member_id, loan.book_id, loan.loan_date, loan.return_date])

def load_books(filename="books.csv"): 
    books = []
    try:
        with open (filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:

                book = Book(row["Book ID"], row["Title"], row["Author"], int(row["Year"]))
                book.is_available = row["Available"].strip() == "True"
                books.append(book)
    except FileNotFoundError:
        print("Books file not found.")
    return books 

def load_members(filename="members.csv"):
    members = []
    try:
        with open (filename, mode = "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                member = Member(row["Member ID"],
                                row["Name"],
                                row["Email"])
                members.append(member)

    except FileNotFoundError:
        print("Members file not found.")

    return members   

def load_loans(filename="loans.csv"):
    loans = []
    try:
        with open (filename, mode="r") as file:
            reader = csv.DictReader(file) 
            for row in reader:
                if row["Return Date"] == "":
                    return_date = None
                else:
                    return_date = row["Return Date"] 
                loan = Loan(row["Loan ID"],
                            row["Member ID"],
                            row["Book ID"],
                            row["Loan Date"],
                            return_date)
                loans.append(loan)
    except FileNotFoundError:
        print("Loans file not found.")   
    return loans 