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

    def search_books(self, query):
        print(f"\n[SEARCH] Searching for query: '{query}'")
        results = []
        for isbn, details in self.books.items():
            if query.lower() in details["title"].lower() or query.lower() in details["author"].lower():
                results.append((isbn, details))
        if not results:
            print(f"No books matched query '{query}'.")
        else:
            for isbn, details in results:
                print(f"  -> Found: [{isbn}] {details['title']} by {details['author']}")
        return results

    def borrow_book(self, isbn):
        # Feature: Express 7-day borrowing policy
        loan_period_days = 7
        late_fee_per_day = 10
        if isbn in self.books and self.books[isbn]["available"]:
            self.books[isbn]["available"] = False
            print(f"[BORROW-EXPRESS] Borrowed '{self.books[isbn]['title']}'. Due in {loan_period_days} days. Late fine: Rs.{late_fee_per_day}/day.")
            return True
        print(f"[BORROW-EXPRESS] Book [{isbn}] is not available.")
        return False


if __name__ == "__main__":
    lib = Library()
    lib.add_book("978-0132350884", "Clean Code", "Robert C. Martin")
    lib.add_book("978-0201616224", "The Pragmatic Programmer", "Andrew Hunt & David Thomas")
    lib.display_books()
    lib.search_books("clean")
