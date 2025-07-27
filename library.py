

class Book:
    def __init__(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.name}  by {self.author} realised on {self.year}"
class Library:
    def __init__(self,name):
        self.name = name
        self.books =[]
    def add_books(self,book):
        self.books.append(book)
        print(f"{book} Added!")
    def remove_books(self,search):
        for book in self.books:
            if book == book.search:
                self.books.remove(book)
        print(f"{search} was successfully removed")
    def search_book(self,book):
        print("$$")
        for fact in self.books:
            if fact.name == book or fact.author == book or fact.year == book:
                print("Book found!")
                print(f"{fact.name} by {fact.author} on {fact.year}")
    def list_books(self):
        if not self.books:
            print("No books registered")
        else:
            print("\n")
            for book in self.books:
                print(f"Name:{book.name} Author:{book.author} Year:{book.year}")

lib = Library("Collection of knowledge")
book1 = Book("1984","George Orwell", "2011")
book2 = Book("A Game of Thrones","George R.R Martine","1996")
lib.add_books(book1)
lib.add_books(book2)
lib.search_book("1984")
lib.list_books()