# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data

import sqlite3

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect("mydatabase.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')
# Insert data
name = input("Enter the name : ")
age = int(input("Enter the age : "))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
# Commit changes
conn.commit()

# flag =  True
# while flag :
#     print("\n1.Insert\n2.Update,\n3.delet,\n4.View All,\n5.exit")
# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data in table
cursor.execute("Update users set name = 'Dip' where id = 5")
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# delet in tabel

cursor.execute("Delete from users where id = 20")
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Close the connection
conn.close()
