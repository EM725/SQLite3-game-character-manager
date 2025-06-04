#inital setup
import sqlite3

db = sqlite3.connect('example.db')

cur = db.cursor()

##create new table
##
##cur.execute("""
##CREATE TABLE IF NOT EXISTS example (
##    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
##    example TEXT NOT NULL,
##    value REAL,
##    mileage INTEGER DEFAULT '0'
##);
##""")
##
##db.commit()
##
##insert record method 1
##cur.execute("""
##INSERT INTO example (example, value, mileage)
##VALUES ('0o0', 10.5, 4)""")
##
##db.commit()
##
##insert record method 2
##cur.execute("""
##INSERT INTO example (example, value, mileage)
##VALUES
##    (?, ?, ?)
##    """, ('woah', 10.75, 5))
##
##db.commit()
##
##method 2 input
##example = input()
##value = input()
##mileage = input()
##cur.execute("""
##INSERT INTO example (example, value, mileage)
##VALUES
##    (?, ?, ?)
##    """, (example, value, mileage))
##
##db.commit()

#query
##cur.execute('SELECT * FROM example WHERE value = 10.5')
##data = cur.fetchall()
##
##for line in data:
##    print(line)


#updating data
##cur.execute("""
##UPDATE example
##SET value = 100
##WHERE id = 2 AND mileage = 200000
##""")
##
##db.commit()

#deleting record
cur.execute("""
DELETE FROM example
WHERE id = 1
""")

db.commit()

#close database
db.close()
