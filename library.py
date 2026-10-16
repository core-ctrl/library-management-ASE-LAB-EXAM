"""
Library Management System
ASE Lab Exam - Gitflow & Merge Conflict Demonstration
"""

class Library:
    def __init__(self, name="Central University Library"):
        self.name = name
        self.books = {}

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            print(f"[ERROR] Book with ISBN {isbn} already exists.")
            return False
        self.books[isbn] = {
            "title": title,
            "author": author,
            "available": True
        }
        print(f"[SUCCESS] Added '{title}' by {author} (ISBN: {isbn})")
        return True

    def display_books(self):
        print(f"\n--- {self.name} Catalog ---")
        if not self.books:
            print("No books in library catalog.")
            return
        for isbn, details in self.books.items():
            status = "Available" if details["available"] else "Borrowed"
            print(f"- [{isbn}] {details['title']} by {details['author']} ({status})")


if __name__ == "__main__":
    lib = Library()
    lib.add_book("978-0132350884", "Clean Code", "Robert C. Martin")
    lib.add_book("978-0201616224", "The Pragmatic Programmer", "Andrew Hunt & David Thomas")
    lib.display_books()
