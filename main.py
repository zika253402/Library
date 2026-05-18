from services.library_manager import LibraryManager
from services.file_manager import load_books, save_books, export_available_books

library = LibraryManager()
library.books = load_books("data/books.csv")

while True:
    print("\n1. Show books")
    print("2. Borrow book")
    print("3. Show overdue")
    print("4. Exit\n")

    choice = input("Choice: ")

    if choice == "1":
        library.show_books()

    elif choice == "2":
        rid = input("Reader ID: ")
        isbn = input("ISBN: ")
        date = input("Return date (YYYY-MM-DD): ")
        library.borrow_book(rid, isbn, date)

    elif choice == "3":
        library.show_overdue()

    elif choice == "4":
        save_books("data/books.csv", library.books)
        export_available_books(library.books)
        print("Goodbye!")
        break