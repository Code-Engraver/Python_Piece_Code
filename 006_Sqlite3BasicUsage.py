# https://portableapps.com/download
# This file introduces the basic use method of sqlite3. 
# The above link is a useful tool when used with sqlite3. 
# I recommend it because it is light and easy.

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_path(*args):
    return os.path.join(BASE_DIR, *args)

# Sample code for inserting dates
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time : {now}")

# Sqlite3 is built-in by default in more than a certain version of Python.
import sqlite3

# Print out the version and check if the import went well.
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version :', sqlite3.sqlite_version)

# More important than the use of sqlite3 is the concept of DB. 
# I can't deal with everything about DB in this file, but I'll try to explain only the important parts.

# First, the concept of commit and rollback. 
# Dealing with DB data is a very important task. 
# Incorrect insertion or modification may break the integrity of the DB, causing serious errors. 
# Therefore, wait for all tasks to be completed normally without reflecting them in the DB. 
# If there is a problem on the way, use rollback to return to the pre-work state. 
# If all work is completed normally, it can be reflected in DB through commit.

# Second, as with I/O, the connection should be closed when the operation is finished.

# The third is for type type sqlite3. 
# Unlike other DBs, sqlite3 has a simple type. 
# It is simplified with TEXT, NUMERIC, INTEGER, REAL and BLOB, making it easy to use.

# Create and connect DBs. 
# If you go to the folder after execution, the DB file is created with the specified name. 
# If the isolation_level=None is specified later, it becomes AUTO_COMMIT without having to commit each time. 
# AUTO_COMMIT is not recommended.
conn = sqlite3.connect(get_path('datasets', '006_database.db'))

# You can execute sql statement using cursor object.
cur = conn.cursor()

# Delete a table for the same exercise each time
cur.execute("""
    DROP TABLE IF EXISTS user
""")

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        regdate TEXT
    )
""")

# You can get information about the table information is available.
# Result configuration : cid, name, type, notnull, dflt_value, pk
cur.execute("""
    pragma table_info(user)
""")
print("\nTable Information")
for cid, name, tp, notnull, dflt_value, pk in cur.fetchall():
    print(f"cid:{cid}, name:{name}, type:{tp}, dflt_value:{dflt_value}, pk:{pk}")

# The method of binding data to sql to the sql to be introduced from now on is the same for all CRUD.
# Sql binding 1
cur.execute("""
    INSERT INTO user (id, name, email, regdate)
    VALUES (?, ?, ?, ?)
""", (1, "Bonita", "Bonita@example.com", now))
conn.commit()

# Sql binding 2
cur.execute("""
    INSERT INTO user (id, name, email, regdate)
    VALUES (:id, :name, :email, :regdate)
""", {"id":2, "name":"Bono", "email":"Bono@example.com", "regdate":now})
conn.commit()

# Insert Many
user_list = (
    (3, "Belita", "Belita@example.com", now),
    (4, "Charlotte", "Charlotte@example.com", now),
    (5, "Cynthia", "Cynthia@example.com", now)
)
cur.executemany("""
    INSERT INTO user (id, name, email, regdate)
    VALUES (?, ?, ?, ?)
""", user_list)
conn.commit()

# Select Many
def show_select_all(msg="\nAll User List"):
    cur.execute("""
        SELECT id, name, email, regdate
        FROM user
    """)
    print(msg)
    for data in cur.fetchall():
        print(data)
show_select_all()

# Select One
def show_select_one(pk, msg="\nOne User"):
    cur.execute("""
        SELECT id, name, email, regdate
        FROM user
        WHERE id = ?
    """,(pk,))
    print(msg)
    print(cur.fetchone())
show_select_one(2)

# Update One
# || This acts like a Concat function.
show_select_one(3, "\nBefore Update")
cur.execute("""
    UPDATE user
    SET name = :name, email = :name || '@example.com'
    WHERE id = :id
""", {"name":"Emma", "id":3})
conn.commit()
show_select_one(3, "After Update")

# Update Many
update_user_list = [
    {"name":"Erica", "id":1},
    {"name":"Frances", "id":2},
    {"name":"Edith", "id":4},
]
show_select_all("\nBefore Update many")
cur.executemany("""
    UPDATE user
    SET name = :name, email = :name || '@example.com'
    WHERE id = :id
""", update_user_list)
conn.commit()
show_select_all("After Update many")

# Delete
show_select_one(3, "\nBefore Delete")
cur.execute("""
    DELETE FROM user
    WHERE id = ?
""",(3,))
conn.commit()
show_select_one(3, "After Delete")

# Create Dump File
with open(get_path('datasets', '006_dump.sql'), "w") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

# Always close the finished connection.
conn.close()
