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
                    book_id, title, author, quantity = line.split()

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

users_dict = load_user()
print(users_dict)
register_user(users_dict)