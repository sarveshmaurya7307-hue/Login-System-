
import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store users in a dictionary {username: hashed_password}
users = {}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists! Try again.")
        return
    password = input("Enter a new password: ")
    users[username] = hash_password(password)
    print("User registered successfully!\n")

# Function to login user with limited attempts
def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == hash_password(password):
            print(f"Welcome, {username}! Login successful \n")
            return True
        else:
            attempts -= 1
            print(f"Invalid username or password. Attempts left: {attempts}\n")

    print("Too many failed attempts . Access denied.\n")
    return False

# Main program
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
