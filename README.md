# 🔐 Python Login System

A simple **User Registration and Login System** built using **Python**. This project demonstrates user authentication by securely storing passwords using **SHA-256 hashing** from Python's `hashlib` library.

## 🚀 Features

- 👤 User Registration
- 🔑 Secure Password Hashing (SHA-256)
- 🔒 User Login Authentication
- ⏳ Maximum 3 Login Attempts
- 📂 Simple Dictionary-Based User Storage
- 💻 Command Line Interface (CLI)

## 🛠️ Technologies Used

- Python 3
- hashlib (Built-in Python Library)

## 📂 Project Structure

```
Python_Login_System/
│── login_system.py
│── README.md
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Python_Login_System.git
```

2. Navigate to the project folder

```bash
cd Python_Login_System
```

3. Run the program

```bash
python login_system.py
```

## 📖 How It Works

### Register
- Enter a unique username.
- Enter a password.
- The password is hashed using SHA-256 before being stored.

### Login
- Enter your username and password.
- The entered password is hashed and compared with the stored hash.
- Users get **3 attempts** to log in successfully.

## 🔒 Security

Passwords are **never stored in plain text**. They are converted into a secure **SHA-256 hash** using Python's `hashlib` module.

## 📸 Sample Output

```
1. Register
2. Login
3. Exit
Enter your choice: 1

Enter a new username: sarvesh
Enter a new password: 12345

User registered successfully!

1. Register
2. Login
3. Exit
Enter your choice: 2

Enter username: sarvesh
Enter password: 12345

Welcome, sarvesh! Login successful
```

## 📌 Future Improvements

- Store user data in a database (SQLite/MySQL)
- Password strength validation
- Forgot Password feature
- Email verification
- Graphical User Interface (Tkinter/PyQt)
- Hide password input using the `getpass` module

## 👨‍💻 Author

**Sarvesh Maurya**

- GitHub: https://github.com/sarveshmaurya7307-hue

---

⭐ If you found this project helpful, don't forget to **Star** the repository!
