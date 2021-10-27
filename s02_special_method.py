# All method start with __XXXX__ this is special method
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {} Pages: {}".format(self.title, self.author, self.pages)

    def __del__(self):
        print("A book is destroyed!")

    def __len__(self):
        return self.pages


b = Book("Muna", "Laxmi", 200)

print(len(b))
