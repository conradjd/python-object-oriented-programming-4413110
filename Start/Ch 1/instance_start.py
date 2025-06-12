# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.__secret = "This is a secret attribute"

    def return_price(self):
        if hasattr(self, "_discount"):
            self.price = self.price - (self.price * self._discount)
            return self.price
        return self.price
    
    def get_discount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", 200)
b2 = Book("The Catcher in the Rye", 150)

# print (f"The original price for book 1 is {b1.return_price()}")
# b1.get_discount(0.1)
# print (f"The price after discount for book 1 is {b1.return_price()}")
# b1.get_discount(0.15)
# print (f"The price after final discount for book 1 is {b1.return_price()}")

print(b1._Book__secret)
print(type(b1._Book__secret))
print(isinstance(b1, Book))

# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
