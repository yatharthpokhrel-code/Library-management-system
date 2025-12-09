
"""
Library management system 
(register, login) --> user
(add book, issue book, return book, view book, search book)
"""

### Creating two file named users.txt and books.txt to store user information and books information permanently inside the file

import os

if not os.path.exists('users.txt'):
    with open('users.txt', 'w') as f:
        pass
if not os.path.exists('books.txt'):
    with open('books.txt', 'w') as f:
        pass

### load data from the file
def load_user():
    """Load all the users from user.txt into dictionary"""
    users_dict = {}

    try:
        with open('users.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(',')
                    users_dict[username] = password
    except FileNotFoundError:
        print("File not found!")
    
    return users_dict

# book_id,title,author,quantity

def load_books():
    books_list = []
    try:
        with open("books.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id, title, author, quantity = line.split(',')

                    book = {
                        'id': book_id,
                        'title': title,
                        'author': author,
                        'quantity': int(quantity)
                    }
                    books_list.append(book)

    except FileNotFoundError:
        print("file not found!")
    return books_list

                    
def get_existing_books_id(books_list):
    """Create a set to store all the ids of the books"""
    book_ids = set()
    for book in books_list:
        # dictionary
        book_ids.add(book['id'])
    return book_ids

#### User registration
def register_user(users_dict):
    """Register a new user"""
    print("\n---- Register a New user ----")
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()
    if username in users_dict:
        print(f"username alrealy exists!")
        return False
    if not username or not password:
        print("Username and password cannot be empty")
        return False
    users_dict[username] = password

    # save the registered user to the file 'users.txt'
    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

    print("registration successfull!")
    return True

# users_dict = load_user()
# print(users_dict)
# register_user(users_dict)


def login_user(users_dict):
    print("\n----- Login User -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users_dict and users_dict[username] == password:
        print(f"Welcome! {username.capitalize()}")
        return username
    else:
        print("Invalid username or password!")
        return None
    

# login_user(users_dict)


###Now books operation start
### Main menu function
def main_menu():
    """Display main menu options"""
    print("="*55)
    print("\nLibrary Management system")
    print("="*55)
    print("1. Add Book")
    print("2. View all books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Logout")
    print("="*55)

# main_menu()


# add book
def add_book(books_list, book_ids):
    """Add a new book to the library"""
    print("\n----- Add New book -----")
    book_id = input("Enter the Book ID: ").strip()

    if book_id in book_ids:
        print("Book id already exist!")
        return
    
    title = input("Enter the book title: ").strip()
    author = input('Enter the author: ').strip()
    quantity = int(input("Entet the quantity: ").strip())

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }

    books_list.append(new_book)
    book_ids.add(book_id)

    with open('books.txt', 'a') as f:
        f.write(f"{book_id},{title},{author},{quantity}\n")

    print("Book added successfully")

# books_list = load_books()
# book_ids = get_existing_books_id(books_list)
# print(books_list)
# print(book_ids)
# add_book(books_list, book_ids)

### Function to view all the books in the library"""
def view_books(books_list):
    """Display all the books in the library"""
    print("\n ----- All book in library -----")
    if not books_list:
        print("No books found in library!")
        return
    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['quantity']}")
# view_books(books_list)


### search a book using title or author
def search_books(books_list):
    found_items = []
    """Search books by book title or author name"""
    search_term = input("Search here: ").strip().lower()

    for book in books_list:
        if search_term in book['title'].lower() or search_term in book['author'].lower():
            found_items.append(book)
    if found_items:
        print(f"Found {len(found_items)} books")
        view_books(found_items)

    else:
        print("No books available")
    
# search_books(books_list)

# save books to the file
def save_books(books_list):
    """Write all books back to books.txt"""
    with open("books.txt", "w") as f:
        for book in books_list:
            f.write(f"{book['id']},{book['title']},{book['author']},{book['quantity']}\n")


### Issue book -> user le library bata book lanu
def  issue_book(books_list):
    book_id = input("Enter the book id to issue: ").strip()

    for book in books_list:
        if book['id'] == book_id:
            if book['quantity'] > 0:
                book['quantity'] -= 1

                save_books(books_list)
                print(f"Book {book['title']} issued successfully!")
                print(f"Remaining quantity: {book['quantity']}")
                return
            else:
                print("Book is currently out of stock!")
                return 
    print("Book id not found!")

def return_book(books_list):
    """Return a book to a user"""
    book_id = input("Enter the book id to return: ").strip()
    for book in books_list:
        if book['id'] == book_id:
            book['quantity'] += 1

            save_books(books_list)

            print(f"Book {book['title']} returned successfully!")
            print(f"Current quantity: {book['quantity']}")
            return
    print("Book id not found")
# add_book(books_list, book_ids)
# issue_book(books_list)
# return_book(books_list)


#### Main function ---> control overall program flow
def main():
    "Main program loop"
    users_dict = load_user()

    print("="*50)
    print("---- Welome to Library Management System ----")
    print("="*50)

    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")
        
        choice = input("\nEnter choice(1,2,3): ").strip()
        
        if choice == '1':
            register_user(users_dict)

        elif choice == '2':
            username = login_user(users_dict)

            if username:
                books_list = load_books()
                book_ids = get_existing_books_id(books_list)

                while True:
                    main_menu()
                    menu_choice = input("\nEnter choice (1-6): ")
                    if menu_choice == '1':
                        add_book(books_list, book_ids)
                    elif menu_choice == '2':
                        view_books(books_list)
                    elif menu_choice == '3':
                        search_books(books_list)
                    elif menu_choice == '4':
                        issue_book(books_list)
                    elif menu_choice == '5':
                        return_book(books_list)
                    elif menu_choice == '6':
                        print(f"Bye {username.capitalize()}!")
                        break
                    else:
                        print("Invalid choice!")

        elif choice == '3':
            print("Thankyou for using my library management system")
            break
        else:
            print('Invalid choice!')


if __name__ == "__main__":
    main()



    # print("1. Add Book")
    # print("2. View all books")
    # print("3. Search Book")
    # print("4. Issue Book")
    # print("5. Return Book")
    # print("6. Logout")