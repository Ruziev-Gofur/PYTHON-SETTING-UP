class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.copies > 0:
            self.books_borrowed.append(book.title)
            book.update_copies(-1)
        else:
            print(f"Sorry {self.name} we don't have {book.title}")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_copies(1)
        else:
            print(f"Sorry {self.name} we don't borrowed {book.title}")

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def display_info(self):
        return (f"\tTitle: {self.title}\n\tAuthor:{self.author}"
                f"\n\tISBN: {self.isbn}\n\tCOPS: {self.copies}")

    def update_copies(self, change):
        self.copies += change

book1 = Book("1984", "George Orwell", "12345", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890", 3)
book3 = Book("The Great Gatsby", "F Scott Fitzgerald", "54321", 4)

# print(book3.display_info())
# # book3.update_copies(6)
# book3.copies += 9
# print(book3.display_info())

member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

print("Before Borrowing")
print(book1.display_info())
print()
print(book2.display_info())

print('-' * 50)
member1.borrow_book(book1)
member2.borrow_book(book2)

print("After Borrowing")
print(book1.display_info())
print()
print(book2.display_info())

