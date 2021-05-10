import sqlite3

db = sqlite3.connect('python_programming')
cursor = db.cursor() #The cursor object is being created

"""
Here we are creating the table using the cursor object
"""
cursor.execute(""" CREATE TABLE python_programming(
					id int PRIMARY KEY,
					name char(50),
					grade int)
				"""
)
print("Table created successfully")
"""
Here we are saving the changes we made to the database
"""
db.commit()

cursor = db.cursor()

"""
Here we are inputting data into the table 
This puts a lot of data at once
"""
student = [(55, 'Carl Davis',61),(66,'Dennis Fredrickson',88),(77,'Jane Richards',78),(12,'Peyton Sawyer',45),(2,'Lucas Brooke',99)]

cursor.executemany("""INSERT INTO python_programming (id, name, grade)
					VALUES(?,?,?)
					""", student
)

db.commit()

print("Data successfully inputted")
cursor = db.cursor()
print("Select all records with a grade between 60 and 80")
"""
Select all records with a grade between 60 and 80
"""
cursor.execute(""" SELECT * FROM python_programming
				WHERE grade >= ?
				AND grade <= ? """, (60,80))
				
for row in cursor:
	print('{0} : {1} : {2}'.format(row[0],row[1],row[2]))
	
db.commit()

cursor = db.cursor()

print("Changed Carl Davis’s grade to 65")

cursor.execute(""" UPDATE python_programming
				SET grade = ?
				WHERE id = ?""", (65,55))
				
db.commit()

cursor = db.cursor()

"""
Delete Dennis Fredrickson's row
"""
cursor.execute(""" DELETE FROM python_programming 
				WHERE id = ? """, (66,))

db.commit()
"""
Change the grade of all people with an id below than 55
"""
cursor.execute(""" UPDATE python_programming 
				SET grade = ?
				WHERE id < ?""", (50,55))
				
db.commit()

print("Grades updated")
