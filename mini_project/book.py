class Book:
    def __init__ (self, title, author, genre, publication_date, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = availability_status

    def borrowed_book (self):
        self.availability_status = "Borrowed"

    def return_book (self):
        self.availability_status = "Availablr"
   

    def adding():
        title = input ("What's the title of the book? ")
        author = input ("What is the author name of the book? ")
        genre = input ("What is the genre? ")
        publication_date = input("What is the publication date? ")
        availablity_status = input ("Is the book available? (yes/no): ").lower()

    
        if availablity_status == 'yes':
           availablity_status = 'available'
        
        else:
            availablity_status = "not available"
        return Book(title, author, genre, publication_date, availablity_status)
            
        
     
    def view (self):
        user_input = input ("View all books by titles? (yes/no)").lower()
       
        if user_input == "yes":
             users = input ("Enter the title of the book: ")
             if users.lower() == self.title:
                print(f"Title: {self.title}, Author: {self.author}, Availbility: {self.availability_status}")
             else: 
                 print("Book is not found.")
        else:
            print("Have a great day.")

    
book = Book.adding()
book.view()

print(f"Book: {book.title}, Author: {book.author}, Availability: {book.availability_status}" )