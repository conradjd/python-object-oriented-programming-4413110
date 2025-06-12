# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    BOOK_TYPES = ("E-BOOK", "ENCLYCLOPEDIA", "HARDCOVER")

    __booklist = None

    @classmethod
    def get_booktypes(cls):
        return cls.BOOK_TYPES

    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype in Book.BOOK_TYPES:
            self.booktype = booktype
        else:
            raise ValueError(f"Booktype {booktype} not recognised")


# TODO: access the class attribute
print(f"Book Types are: {Book.get_booktypes()}")

b1 = Book("Title1", "HARDCOVER")
print(f"Book with title {b1.title} and booktype {b1.booktype}")
b2 = Book("Title2", "E-BOOK")
print(f"Book with title {b2.title} and booktype {b2.booktype}")


thebooks = Book.get_booklist()
print(thebooks)
thebooks.append(b1.title)
thebooks.append(b2.title)
print(thebooks)

