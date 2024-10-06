import sqlite3

def add_user(name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()       
        cursor.execute('''   
        INSERT INTO employee (name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary))
        print(f"User {name} added successfully.")

def view_users():
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee')
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Role: {row[3]}, Department ID: {row[4]}, Email: {row[5]}, Contact: {row[6]}, Enrolment Date: {row[7]}, Salary: {row[8]}")
        else:
            print("No users found.")

def update_user(employee_ID, name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor() 
        cursor.execute('''
        UPDATE employee
        SET name = ?, age = ?, role_varchar = ?, department_ID = ?, employee_email = ?, employee_contact_number = ?, enrolment_date = ?, salary = ?
        WHERE employee_ID = ? 
        ''', (name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary, employee_ID))
        print(f"User ID {employee_ID} updated successfully.")

def delete_user(employee_ID):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM employee WHERE employee_ID = ?', (employee_ID,))
        print(f"User ID {employee_ID} deleted successfully.")

def add_department(department_name, health_insurance, bonuses, training_sessions, performance_reviews):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO departments (department_name, health_insurance, bonuses, training_sessions, performance_reviews)
        VALUES (?, ?, ?, ?, ?)
        ''', (department_name, health_insurance, bonuses, training_sessions, performance_reviews))
        print(f"Department {department_name} added successfully.")

def view_departments():
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM departments')
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"Department ID: {row[0]}, Name: {row[1]}, Health Insurance: {row[2]}, Bonuses: {row[3]}, Training Sessions: {row[4]}, Performance Reviews: {row[5]}")
        else:
            print("No departments found.")

def update_department(department_ID, department_name, health_insurance, bonuses, training_sessions, performance_reviews):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE departments
        SET department_name = ?, health_insurance = ?, bonuses = ?, training_sessions = ?, performance_reviews = ?
        WHERE department_ID = ?
        ''', (department_name, health_insurance, bonuses, training_sessions, performance_reviews, department_ID))
        print(f"Department ID {department_ID} updated successfully.")

def delete_department(department_ID):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM departments WHERE department_ID = ?', (department_ID,))
        print(f"Department ID {department_ID} deleted successfully.")

def search_department_by_employee_name(name):
    with sqlite3.connect('employee_management_database.db') as conn:
        cursor = conn.cursor()
        query = '''
        SELECT e.name, d.department_name
        FROM employee e
        JOIN departments d ON e.department_ID = d.department_ID
        WHERE e.name LIKE ?
        '''
        cursor.execute(query, ('%' + name + '%',))
        results = cursor.fetchall()

        if results:
            for result in results:
                print(f"Employee: {result[0]}, Department: {result[1]}")
        else:
            print("No matching employee found.")

def update_employee_role_by_id(employee_id, new_role):
    try:
        with sqlite3.connect('employee_management_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE employee
            SET role_varchar = ?
            WHERE employee_ID = ?
            ''', (new_role, employee_id))
            print(f"Employee with ID {employee_id} role updated to {new_role}.")
    except sqlite3.Error as error:
        print("Error updating employee role:", error)

def main():

    while True: 
        print("\n1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Add Department")
        print("6. View Departments")
        print("7. Update Department")
        print("8. Delete Department")
        print("9. Search Employee by Name")
        print("10. Update Employee Role")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")  
            age = int(input("Enter age: "))
            role_varchar = input("Enter role: ")
            department_ID = int(input("Enter department ID: "))
            employee_email = input("Enter email: ")
            employee_contact_number = input("Enter contact number: ")
            enrolment_date = input("Enter enrolment date (YYYY-MM-DD): ")
            salary = int(input("Enter salary: "))
            add_user(name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary)

        elif choice == '2':
            view_users()

        elif choice == '3':
            employee_ID = int(input("Enter employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            role_varchar = input("Enter new role: ")
            department_ID = int(input("Enter new department ID: "))
            employee_email = input("Enter new email: ")
            employee_contact_number = input("Enter new contact number: ")
            enrolment_date = input("Enter new enrolment date (YYYY-MM-DD): ")
            salary = int(input("Enter new salary: "))
            update_user(employee_ID, name, age, role_varchar, department_ID, employee_email, employee_contact_number, enrolment_date, salary)

        elif choice == '4':
            employee_ID = int(input("Enter employee ID to delete: "))
            delete_user(employee_ID)

        elif choice == '5':
            department_name = input("Enter department name: ")
            health_insurance = input("Enter health insurance details (Yes/No): ")
            bonuses = int(input("Enter bonuses amount ($): "))
            training_sessions = int(input("Enter total training sessions: "))
            performance_reviews = input("Enter performance review (scores): ")
            add_department(department_name, health_insurance, bonuses, training_sessions, performance_reviews)

        elif choice == '6':
            view_departments()

        elif choice == '7':
            department_ID = int(input("Enter department ID to update: "))
            department_name = input("Enter new department name: ")
            health_insurance = input("Enter new health insurance details (Yes/No): ")
            bonuses = int(input("Enter new bonuses amount ($): "))
            training_sessions = int(input("Enter new total training sessions: "))
            performance_reviews = input("Enter new performance review (scores): ")
            update_department(department_ID, department_name, health_insurance, bonuses, training_sessions, performance_reviews)

        elif choice == '8':
            department_ID = int(input("Enter department ID to delete: "))
            delete_department(department_ID)

        elif choice == '9':
            search_name = input("Enter employee name to search for: ")
            search_department_by_employee_name(search_name)

        elif choice == '10':
            employee_id = int(input("Enter the ID of the employee to update role: "))
            new_role = input("Enter the new role: ")
            update_employee_role_by_id(employee_id, new_role)

        elif choice == '11':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()