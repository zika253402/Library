import csv
from models.book import Book, SpecialBook

def load_books(filename):
    books = []
    file = open(filename, newline="")
    reader = csv.DictReader(file)

    for row in reader:
        if "category" in row and row["category"] == "reference":
            book = SpecialBook(
                row["title"],
                row["isbn"],
                row["author"],
                int(row["year"]),
                int(row["copies"]),
                row["category"]
            )
        else:
            book = Book(
                row["title"],
                row["isbn"],
                row["author"],
                int(row["year"]),
                int(row["copies"])
            )
        books.append(book)

    file.close()
    return books


def save_books(filename, books):
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "isbn", "author", "year", "copies"])

    for book in books:
        writer.writerow([book.title, book.isbn, book.author, book.year, book.copies])

    file.close()


def export_available_books(books):
    available = list(filter(lambda b: b.copies > 0, books))

    file = open("available_books.txt", "w")
    for book in available:
        file.write(book.title + "\n")
    file.close()


def export_book_titles(books):
    titles = list(map(lambda b: b.title, books))

    file = open("book_titles.txt", "w")
    for title in titles:
        file.write(title + "\n")
    file.close()