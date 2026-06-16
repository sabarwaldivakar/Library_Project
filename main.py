from book import Book
from member import Member
from library import Library
from storage import (
load_books,
load_members,
load_loans,
save_books,
save_members,
save_loans,)

library = Library("City Library")

library.books=load_books()
library.members=load_members()
library.loans=load_loans()
for loan in library.loans:
    if loan.is_active():
        for member in library.members:
            if member.member_id == loan.member_id:
                member.borrow_book(loan.book_id)
                break
while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Members")
    print("7. Display Loans")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        book_id = library.generate_book_id()
        print (f"Generated Book ID: {book_id}")
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        try:
             year = int(input("Enter Year: "))
        except ValueError:
            print ("Invalid entry. Please enter a valid year")
            continue
        book = Book(book_id, title, author, year)
        library.add_book(book)

    elif choice == "2":
        member_id = library.generate_member_id()
        print (f"Generated Member ID; {member_id}")

        try:
            name = input("Enter Name: ").strip()
            if not name.replace(" ", "").isalpha():
                raise ValueError
        except:
            print ("Name must be only alphabets")
        email = input("Enter Email: ").strip()

        member = Member(member_id, name, email)
        library.add_member(member)

    elif choice == "3":
        member_id = input("Enter Member ID: ").strip()
        book_id = input("Enter Book ID: ").strip()

        library.borrow_book(member_id, book_id)
    elif choice == "4":
         member_id = input("Enter Member ID: ").strip()
         book_id = input ("Enter Book ID: ").strip()

         library.return_book(member_id, book_id)

    elif choice == "5":
        library.display_books()
    elif choice == "6":
        library.display_members()
    elif choice == "7":
        library.display_loans()
    elif choice == "8":
        save_books(library.books)
        save_members(library.members)
        save_loans(library.loans) 
        print("Data saved successfully")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        

