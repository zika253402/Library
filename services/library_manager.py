from datetime import datetime, date
from models.reader import Reader
from models.loan import Loan
from utils.validators import valid_isbn
from utils.decorators import log_action


class LibraryManager:
    def __init__(self):
        self.books = []
        self.readers = []
        self.loans = []

    def show_books(self):
        for book in self.books:
            print(book.title, "-", book.copies)

    @log_action
    def borrow_book(self, reader_id, isbn, return_date):

        if not valid_isbn(isbn):
            print("Invalid ISBN")
            return

        for book in self.books:
            if book.isbn == isbn and book.is_available():

                reader = Reader(reader_id, "Reader " + reader_id)
                self.readers.append(reader)

                date = datetime.strptime(return_date, "%Y-%m-%d").date()

                loan = Loan(reader, book, date)
                self.loans.append(loan)

                book.copies -= 1

                print("Book borrowed")
                return

        print("Book not available")

    def show_overdue(self):
        today = date.today()
        found = False

        for loan in self.loans:
            if loan.return_date < today:
                print(
                    loan.book.title,
                    "-",
                    loan.reader.name,
                    "-",
                    loan.return_date
                )
                found = True

        if not found:
            print("No overdue books")