class Book:
    def __init__(self, title, isbn, author, year, copies):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.year = year
        self.copies = copies

    def is_available(self):
        if self.copies > 0:
            return True
        return False


class SpecialBook(Book):
    def __init__(self, title, isbn, author, year, copies, category):
        Book.__init__(self, title, isbn, author, year, copies)
        self.category = category

    def is_available(self):
        if self.copies > 0 and self.category != "reference":
            return True
        return False