from datetime import date

class Loan:
    def __init__(self, reader, book, return_date):
        self.reader = reader
        self.book = book
        self.borrow_date = date.today()
        self.return_date = return_date

    def is_overdue(self):
        if date.today() > self.return_date:
            return True
        return False