# Problems:
class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf
o1 = Library(300, 45)
# print(o1.book)
# print(o1.shelf)

class science_section(Library):
    def __init__(self, book, shlef, name):
        super().__init__(book, shlef)
        self.name = name

    def print(self):
        print("No. of books is", self.book,
              "No. of shelf is", self.shelf,
              "And Type of books is", self.name)
x = science_section(20, 4, "Physics books")
print(x.name)
x.print()

