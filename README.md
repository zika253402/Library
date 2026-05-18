# Library Management System

## Project Description
This is a simple Library Management System written in Python.

The system allows users to manage books, readers, and borrowing operations using a console menu.

The project is based on Object-Oriented Programming (OOP), file handling, decorators, regex validation, and unit testing.

---

## Features

- Show all books
- Borrow books
- Check overdue books
- Validate ISBN numbers
- Load books from CSV file
- Save updated books to CSV
- Export available books to TXT
- Export overdue books to TXT
- Logging using decorator
- Unit testing

---

## Project Structure
library_system/
├── data/
│ └── books.csv
├── models/
│ ├── book.py
│ ├── __init__.py
│ ├── reader.py
│ └── loan.py
├── services/
│ ├── library_manager.py
│ ├── __init__.py
│ └── file_manager.py
├── utils/
│ ├── decorators.py
│ ├── __init__.py
│ └── validators.py
├── tests/
│ └── test_library.py
├── available_books.txt
├── main.py
├── requirements.txt
└── README.md

---

## Classes

### Book
Represents a book in the library:
- title
- isbn
- author
- year
- copies

### Reader
Represents a library user:
- reader_id
- name

### Loan
Represents borrowing process:
- reader
- book
- borrow_date
- return_date

### LibraryManager
Main system logic:
- show books
- borrow books
- show overdue books

### FileManager
Handles file operations:
- load books from CSV
- save books to CSV
- export TXT reports

---

## How to Run

1. Open terminal
2. Go to project folder
3. Run:

python main.py

---

## Menu Example

1. Show all books
2. Borrow a book
3. Show overdue books
4. Save & Exit

---

## Example books.csv

title,isbn,author,year,copies
Harry Potter,1234567890123,J.K. Rowling,1997,3
Hobbit,9780261102217,Tolkien,1937,2

---

## Testing

Run tests with:

python -m unittest tests/test_library.py

---

## Future Improvements

- Add return book feature
- Add GUI interface
- Connect SQLite database
- Add search system
- Add authentication

---

## Author

## Team Contributions

The project was developed collaboratively by Zamira and Zeyne.

### Zamira
Focused on:
- Project architecture
- Core models (Book, Reader)
- Main application flow
- Validation logic
- Documentation and README

### Zeine
Focused on:
- Business logic (LibraryManager)
- Loan management
- File management system
- Logging decorators
- Unit testing
- Data export functionality