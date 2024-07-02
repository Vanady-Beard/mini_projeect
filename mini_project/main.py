from mini_project.book import Book, add_book
from mini_project.author import Author, add_author
from mini_project.user import Users, add_user

def main_menu():
    while True:
        user_input = input('''
Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

 ''')

        if user_input == '1':
            book_operations()
        elif user_input == '2':
            user_operations()
        elif user_input == '3':
            author_operations()
        elif user_input == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option (1/2/3/4).")

def book_operations():
    while True:
        user_input = input('''
    Book Operations Menu:

    1. Add a New Book
    2. View All Books
    3. Back to Main Menu
 ''')

        if user_input == '1':
            book = add_book()
            print(f"Book '{book.title}' added successfully!")
        elif user_input == '2':
          
            pass
        elif user_input == '3':
            break
        else:
            print("Invalid input. Please enter a valid option (1/2/3).")

def user_operations():
    while True:
        user_input = input('''
    User Operations Menu:

    1. Add a New User
    2. Borrow a Book
    3. Return a Book
    4. View Borrowed Books
    5. Back to Main Menu

 ''')

        if user_input == '1':
            user = add_user()
            print(f"User '{user.name}' added successfully!")
        elif user_input == '2':
           
            pass
        elif user_input == '3':
           
            pass
        elif user_input == '4':
            
            pass
        elif user_input == '5':
            break
        else:
            print("Invalid input. Please enter a valid option (1/2/3/4/5).")

def author_operations():
    while True:
        user_input = input('''
    Author Operations Menu:

    1. Add a New Author
    2. View Author Details
    3. Back to Main Menu

 ''')

        if user_input == '1':
            author = add_author()
            print(f"Author '{author.name}' added successfully!")
        elif user_input == '2':
           
            pass
        elif user_input == '3':
            break
        else:
            print("Invalid input. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main_menu()
