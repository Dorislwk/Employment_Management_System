import sqlite3

def create_table():
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            role_varchar TEXT NOT NULL,
            department_ID INTEGER,
            employee_email TEXT,
            employee_contact_number TEXT,
            enrolment_date DATE,
            salary INTEGER
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            department_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL,
            health_insurance TEXT NOT NULL,
            bonuses INTEGER NOT NULL,
            training_sessions INTEGER,
            performance_reviews TEXT
        )
        ''')

create_table()

def add_user(name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO employee (name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary))
        print(f"User {name} added successfully.") 

def add_department(department_name, health_insurance, bonuses, training_sessions, performance_reviews):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO departments (department_name, health_insurance, bonuses, training_sessions, performance_reviews)               
        VALUES (?, ?, ?, ?, ?)               
        ''',(department_name, health_insurance, bonuses, training_sessions, performance_reviews))
        print(f"{department_name} added successfully")

add_user('John Doe', 30, 'Developer', 1, 'john@example.com', '1234567890', '2024-08-25', 60000)
add_user('Danny Chow', 30, 'Human Resources', 2, 'DannyChow@example.com', '24567890', '2022-09-30', 25000)
add_department('IT Support', 'Yes', 6000, 30, 90)
add_department('Human Resources', 'Yes', 4000, 20, 80)