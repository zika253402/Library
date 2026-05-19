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

## 📁 Project Structure
```
library-system/
│
├── data/
│   └── books.csv
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── reader.py
│   └── loan.py
│
├── services/
│   ├── __init__.py
│   ├── library_manager.py
│   └── file_manager.py
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   └── validators.py
│
├── tests/
│   └── test_library.py
│
├── main.py
├── README.md
└── requirements.txt
```
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
Dracula,9780141439846,Bram Stoker,1897,5
The Cruel Prince,9780316310277,Holly Black,2018,8
The Wicked King,9780316310352,Holly Black,2019,6
The Queen of Nothing,9780316310420,Holly Black,2019,5

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
