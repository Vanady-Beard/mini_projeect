class Users:
    def __init__(self,name, libraryID, borrowed_books):
        self.name = name
        self.libraryID = libraryID
        self.borrowed_books = []


    def borrow_book(self,b_book):
        if b_book.availability_status == "Available":
            b_book.borrow_book()
            self.borrowed_books.append(b_book)
            print(f"{self.name} has borrowed '{b_book.title}'")
        else:
            print("Sorry '{b_book.title}' is not available to borrow at the momment. " )
    
    def returned(self, b_book):
       try: 
            
            if b_book in self.borrowed_books:
             b_book.returm_book()
             self.borrowed_books.remove(b_book)
             print (f"{self.name} has returned '{b_book.title}'")
            else:
                 (f"This book never was borrowed before")
       except Exception as e:
              print(f"Error:{e}")
    
    def view_books(self):
        if self.borrow_book:
            print(f"{self.name} borrowed a book")
            for b_book in self.borrowed_books:
                print(f"Title: {b_book.title}, Author: {b_book.author}, Availability: {b_book.availability_status}")
        else:
            print(f"{self.name} has not borrowed books")
    
    def add_user():
        name = input("What is your name: ")
        library_id = input ("What is your Library ID:")
        return Users(name, library_id)
    
    if __name__ == "__main__":
        users = add_user()
        print(f"User: {users.name}, Library ID: {users.libraryID}")