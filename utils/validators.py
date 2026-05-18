import re

def valid_isbn(isbn):
    if re.match(r"^\d{13}$", isbn):
        return True
    return False