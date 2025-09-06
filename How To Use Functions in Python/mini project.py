from django.template.defaultfilters import title

available_books = []

def add_book(title, author, isbn='0000000000'):
    available_books.append(
        {
            'title': title,
            'author': author,
            'isbn': isbn,
        }
    )
    print(f'\tBoo; added: {title}')

def list_books():
    print("Available books:")
    for book in available_books:
        print(f"\t - {book['title']} by {book['author']} ({book['isbn']}")

def borrow_book(*titles):
    for title in titles:
        for book in available_books:
            if book['title'] == title:
                available_books.remove(book)
                print(f'\tBorrowed Book: {title}')
                break
        else:
            print(f'Book not found: {title}')


sample_book = [
    ("To Kill a Mockingbird", "Narper Lee", "9790446310789"),
    ("Prida", "George Orwell", "9780451524935"),
    ("The Great Gatsby", "Jane Austen", "9780743273565"),
]

for bool in sample_book:
    add_book(bool[0], bool[1], bool[2])

list_books()
borrow_book(
    "Prida",
    "George Orwell",
    "Narper Lee",
)
list_books()





