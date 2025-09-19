import datetime

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_loaned = False
        self.reserved_by = None  

class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name

class Loan:
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower
        self.loan_date = datetime.date.today()
        self.due_date = self.loan_date + datetime.timedelta(days=14)

class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author)

    def search_book(self, book_id):
        return self.books.get(book_id, None)

class BorrowerManager:
    def __init__(self):
        self.borrowers = {}

    def add_borrower(self, borrower_id, name):
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

    def search_borrower(self, borrower_id):
        return self.borrowers.get(borrower_id, None)

class LoanManager:
    def __init__(self):
        self.loans = []

    def create_loan(self, book, borrower):
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        loan = Loan(book, borrower)
        self.loans.append(loan)
        book.is_loaned = True

class LibraryFacade:
    def __init__(self):
        self.book_manager = BookManager()
        self.borrower_manager = BorrowerManager()
        self.loan_manager = LoanManager()

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.book_manager.add_book(book_id, title, author)
        print(f"Book '{title}' added successfully!")

    def add_borrower(self):
        borrower_id = input("Enter borrower ID: ")
        name = input("Enter borrower name: ")
        self.borrower_manager.add_borrower(borrower_id, name)
        print(f"Borrower '{name}' added successfully!")

    def create_loan(self):
        book_id = input("Enter book ID to loan: ")
        borrower_id = input("Enter borrower ID: ")
        book = self.book_manager.search_book(book_id)
        borrower = self.borrower_manager.search_borrower(borrower_id)
        if book and borrower:
            self.loan_manager.create_loan(book, borrower)
            print(f"Book '{book.title}' loaned to '{borrower.name}'.")
        else:
            print("Book or borrower not found.")

# Running the system interactively
library = LibraryFacade()

while True:
    print("\nLibrary System")
    print("1. Add Book")
    print("2. Add Borrower")
    print("3. Loan Book")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.add_borrower()
    elif choice == "3":
        library.create_loan()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
