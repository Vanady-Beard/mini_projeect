


class Author:

    def __init__(self, name, biography):
        self.name = name 
        self.biography = biography
        self.books = []
        
    def author_book(self, book):
        self.books.append(book)

def authors ():
        name = input("What is the author's name: ")
        biography = input("What is the author's biography: ")
        return Author(name, biography)
    
if __name__ == "__main__":

        author_info = authors()

        print(f"Author: {author_info.name}")
        print(f"Biography: {author_info.biography}")
        print("Books written by the author:")