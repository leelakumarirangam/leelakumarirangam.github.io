class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} ({status})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'.")
                return
        print("Book not found or wasn't borrowed.")

# -------- Main Menu --------
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.add_book(title, author)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
