class LibraryBook:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

        LibraryBook.total_books += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def __str__(self):
        return self.title + " by " + self.author

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}')"


# Create book objects
book1 = LibraryBook("Harry Potter", "J.K. Rowling")
book2 = LibraryBook("The Little Prince", "Antoine de Saint-Exupery")

# Display books
print(book1)
print(book2)

# Borrow and return books
book1.borrow()
book1.return_book()

# Display total books
print("Total books:", LibraryBook.total_books)

# Display object representation
print(repr(book1))

