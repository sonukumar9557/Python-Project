# Python-Project
# Registration Form System

A desktop-based Registration Form System developed using Python Tkinter and MySQL. This application allows users to register, update, delete, search, and display records through a graphical user interface.

## Features

- User Registration
- Update Existing Records
- Delete Records
- Search Records
- Display All Records
- Login Window
- Password Hide/Show
- Date Picker using tkcalendar
- MySQL Database Connectivity

## Technologies Used

- Python
- Tkinter
- MySQL
- PyMySQL
- tkcalendar
- Pillow (PIL)

## Required Libraries

Install the required libraries using:

```bash
pip install pymysql tkcalendar pillow
```

## Database

Create a MySQL database named `data` and a table named `registration`.

Example table structure:

```sql
CREATE TABLE registration (
    Name VARCHAR(50),
    Lastname VARCHAR(50),
    Contact BIGINT,
    City VARCHAR(50),
    Email VARCHAR(100) PRIMARY KEY,
    Password VARCHAR(100),
    Date DATE,
    Gender VARCHAR(20)
);
```

## How to Run

1. Clone the repository.
2. Install the required libraries.
3. Create the MySQL database and table.
4. Update the MySQL username and password in the source code.
5. Run:


