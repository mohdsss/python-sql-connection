# 🐍 Python MySQL Sales Management System

A simple **Python + MySQL** project for managing sales data through a menu-driven command-line interface.

## 🚀 Features

* 🔌 Connect Python with MySQL
* ➕ Add a new sale
* 🔍 Search sales using name or ID
* 🗑️ Delete a sale
* 📋 Display sales data
* 🖥️ Menu-driven command-line interface
* 🐍 Uses Python Classes and Methods
* 💾 Uses MySQL database for data storage

## 🛠️ Technologies Used

* Python
* MySQL
* mysql-connector-python

## 📁 Project Structure

```text
Python-MySQL-Sales-Management/
│
├── data.py
├── query.py
└── README.md
```

## ⚙️ Installation

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

Make sure MySQL Server is installed and running.

## 🔗 Database Configuration

The project uses a local MySQL database.

```python
host="localhost"
user="root"
database="safan"
```

Update the database configuration in `data.py` according to your MySQL setup.

> ⚠️ Do not upload your real MySQL password to a public GitHub repository.

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Python-MySQL-Sales-Management
```

### 3. Install Required Package

```bash
pip install mysql-connector-python
```

### 4. Run the Program

Run `data.py`:

```bash
python data.py
```

`data.py` imports the `connect` class from `data.py`, so **both files should be in the same folder**.

You **do not need to run `data.py` separately**.

## 📋 Menu

After running `query.py`, the program provides a menu for performing database operations.

```text
1. Add New Sale
3. Delete Sale
4. Show Sale
```

Enter your choice when prompted.

## ➕ Add New Sale

Choose the Add Sale option and enter:

```text
Enter your name =
Enter your sale =
Enter your city =
```

The data is then inserted into the MySQL database.

## 🔍 Search Sale

The program can search records using:

* Name
* ID
* Name + ID
* All records

The matching records are fetched from MySQL and displayed.

## 🗑️ Delete Sale

Enter the username of the sale you want to delete. The corresponding record is removed from the database.

## 🧠 Concepts Used

* Python OOP
* Classes and Objects
* MySQL Connectivity
* SQL Queries
* INSERT
* SELECT
* DELETE
* Cursor
* `commit()`
* `fetchall()`
* User Input
* Menu-driven Programming

## 🔮 Future Improvements

* Add Update Sale functionality
* Complete the Show Sale option
* Add an Exit option
* Add error handling
* Use parameterized SQL queries
* Add input validation

## 👨‍💻 Author

**Safan**

Built to practice **Python + MySQL + OOP + CRUD operations**.
