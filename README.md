# Python MySQL Database Project

A simple **Python + MySQL** project that demonstrates how to connect Python with a MySQL database and perform basic database operations such as **INSERT, SELECT, fetching particular records, displaying data, and DELETE**.

## 🚀 Features

* Connect Python with MySQL
* Insert data into a MySQL table
* Fetch all records
* Search for a particular record
* Search using name and ID
* Display fetched records
* Delete records by username
* Uses Python OOP (Class & Methods)

## 🛠️ Technologies Used

* Python
* MySQL
* `mysql-connector-python`

## 📁 Project Structure

```text
project/
│
├── data.py
├── query.py
└── README.md
```

## ⚙️ Installation

Install the MySQL connector for Python:

```bash
pip install mysql-connector-python
```

Make sure MySQL Server is installed and running on your computer.

## 🔌 Database Connection

The project connects to a local MySQL database using:

```python
mysql.connector
```

The connection uses:

* Host: `localhost`
* User: `root`
* Database: `safan`

> **Note:** Change the database credentials in the code according to your own MySQL setup. Never upload real passwords to a public GitHub repository.

## ▶️ How to Run

Run the query program:

```bash
python query.py
```

It asks for:

```text
enter name =
enter id =
```

The entered name and ID are then used to search the database and display the matching record.

## 📌 Database Operations

### Insert Data

The project provides an `insertData()` method to insert username, sale, and city data into a selected table.

### Get All Data

The `getData()` method executes a `SELECT *` query and returns all records from a table.

### Find Particular Data

The `particulardata()` method can search:

* All records
* By username
* By ID
* By both username and ID

### Display Data

The `showData()` method loops through the returned records and prints the selected fields.

### Delete Data

The `delete()` method deletes records from the `safan2` table based on username.

## 🧠 Concepts Practiced

This project is useful for learning:

* Python Classes
* Constructors
* Methods
* MySQL connections
* MySQL cursors
* SQL queries
* `SELECT`
* `INSERT`
* `DELETE`
* `commit()`
* `fetchall()`
* Python input handling
* Basic CRUD operations

## 🔮 Future Improvements

* Use parameterized SQL queries
* Add UPDATE operation
* Add better error handling
* Add a menu-driven interface
* Move database credentials to environment variables
* Add proper validation for user input

## 👨‍💻 Author

**Safan**

Built as a beginner project to practice **Python + MySQL database connectivity and CRUD operations**.
