# # 1. Import libraiers:
# import sqlite3
# from sqlite3 import Error
# #
# #
# # ___________________________________________________
# # 2. Create function to create new connection:
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
#
#
# connection = create_connection("data.sqlite")
#
#
# # # # ___________________________________________________
# # 3. Create function to excute queries:
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")


# # ___________________________________________________

# # 4. Create queries for creating tables:
# #
# create_Employees_table = """
# CREATE TABLE IF NOT EXISTS Employees (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT,
#   specialty   TEXT
# );
#  """
#
# create_Position_table = """
# CREATE TABLE IF NOT EXISTS Position(
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   job TEXT
# );
# """
#
# create_Department_table = """
# CREATE TABLE IF NOT EXISTS Department (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   salary TEXT NOT NULL
# );
# """
#
# create_EmplPosition_table = """
# CREATE TABLE IF NOT EXISTS EmplPosition (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   Position_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees (id) FOREIGN KEY (Position_id) REFERENCES Position (id)
# );
# """
#
# create_EmplDepartment_table = """
# CREATE TABLE IF NOT EXISTS EmplDepartment (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   Dep_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees (id) FOREIGN KEY (Dep_id) REFERENCES Department (id)
# );
# """
#
# create_EmplRate_table = """
# CREATE TABLE IF NOT EXISTS EmplRate (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   emply_id INTEGER NOT NULL,
#   rate_id INTEGER NOT NULL,
#   FOREIGN KEY (emply_id) REFERENCES Employees (id)
# );
# """
# execute_query(connection, create_Employees_table)
# execute_query(connection, create_Position_table)
# execute_query(connection, create_Department_table)
# execute_query(connection, create_EmplPosition_table)
# execute_query(connection, create_EmplDepartment_table)
# execute_query(connection, create_EmplRate_table)

# # # ___________________________________________________
# 4. Create INSERT queries:
#
# create_Employees = """
# INSERT INTO
#   Employees (name, age, gender, nationality, specialty)
# VALUES
#   ('Michael ', 45, 'male', 'USA', 'MIS'),
#   ('Pam ', 30, 'female', 'USA', 'IT'),
#   ('Jim ', 27, 'male', 'England', 'CS'),
#   ('Meredith ', 50, 'female', 'France', 'LANGUAGE'),
#   ('Dwight ', 31, 'male', 'Germany', 'HISTORY');
# """
#
# create_Position = """
# INSERT INTO
#   Position (name, job)
# VALUES
#   ("Michael", " Regional Manager"),
#   ("Pam", "Receptionist"),
#   ("Jim", "Salesman"),
#   ("Meredith", "Accountant"),
#   ("Dwight", "Assurance Manager");
# """
# #
# create_Department = """
# INSERT INTO
#   Department (name, salary)
# VALUES
#   ('Michael', '$20k'),
#   ('Pam', '$6k'),
#   ('Jim', '$10'),
#   ('Meredith', '$8'),
#   ('Dwight', '$13K');
# """
# #
# create_EmplPosition = """
# INSERT INTO
#   EmplPosition (emply_id, Position_id)
# VALUES
#   (1, 2300),
#   (2, 1911),
#   (3, 1299),
#   (4, 1822),
#   (5, 2199);
# """
# #
# create_EmplDepartment = """
# INSERT INTO
#   EmplDepartment (emply_id, Dep_id)
# VALUES
#   (1, 7),
#   (2, 11),
#   (3, 11),
#   (4, 9),
#   (5, 7);
# """
# #
# create_EmplRate = """
# INSERT INTO
#   EmplRate (emply_id, rate_id)
# VALUES
#   (1, 67),
#   (2, 78),
#   (3, 92),
#   (4, 55),
#   (5, 85);
# """
# execute_query(connection, create_Employees)
# execute_query(connection, create_Position)
# execute_query(connection, create_Department)
# execute_query(connection, create_EmplPosition)
# execute_query(connection, create_EmplDepartment)
# execute_query(connection, create_EmplRate)

# # ___________________________________________________
# #Create SELECT queries:
#
# select_Position = "SELECT * FROM Position"
# Position = execute_read_query(connection, select_Position)
#
# for pos in Position:
#     print(pos)

# select_EmplRate = "SELECT * FROM EmplRate"
# EmplRate = execute_read_query(connection, select_EmplRate)
#
# for Rate in EmplRate:
#     print(Rate)

# select_Employees_Department = """
# SELECT
# Employees.name, Department.salary
# FROM
# Employees
# JOIN Department ON Employees.id = Department.id
# """
#
# Employees_Department = execute_read_query(connection, select_Employees_Department)
# for Employees_Department in Employees_Department:
#     print(Employees_Department)

#
# #Create SELECT queries with WHERE:

# select_Employees = "SELECT * FROM Employees WHERE gender is 'female'"
#
# Employees = execute_read_query(connection, select_Employees)
#
# for emp in Employees:
#     print(emp)

# select_EmplyRate_Department = """
# SELECT
#     SUM(EmplRate.id) as EmplyRate
# FROM
#     EmplRate
# JOIN
#     Employees ON EmplRate.emply_id = Employees.id
# JOIN
#     EmplDepartment ON Employees.id = EmplDepartment.emply_id
# JOIN
#     Department ON EmplDepartment.Dep_id = Department.id
# """
#
# EmplyRate_Department = execute_read_query(connection, select_EmplyRate_Department)
#
# for dep in EmplyRate_Department:
#     print(dep)

# #  Update records using SELECT:
# select_Position_job = "SELECT job FROM Position WHERE id = 3"
#
# Position_job = execute_read_query(connection, select_Position_job)
# for job in Position_job:
#     print(job)

# update_Position_job = """
# UPDATE
#   Position
# SET
#   job = "General Manger"
# WHERE
#   id = 3
# """
#
# execute_query(connection, update_Position_job)


# # Delete records using SELECT:
# delete_EmplRate = "DELETE FROM EmplRate WHERE id = 4"
# execute_query(connection, delete_EmplRate)


