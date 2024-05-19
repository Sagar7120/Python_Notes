class Library:
    def __init__(self):
        self.Books = []
        self.noofBooks = 0

    def addBooks(self, books):
        self.Books.append(books)
        self.j = (", ".join(self.Books))
        self.noofBooks= len(self.Books)

    def show (self):
        print(f"The books added are {self.j} and the number of books present in the library is {self.noofBooks}")

a = Library()
a.addBooks("Rich Dad Poor Dad")
a.addBooks("Quantum")
a.addBooks("attitude is everything")
a.addBooks("sattle")
a.show()

