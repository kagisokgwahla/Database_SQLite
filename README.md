# SQLite

## Introduction to SQLite

SQLite is built in Python to provide a relational database management system. It is
very easy to set up, very fast and lightweight, and thus referred to as ‘lite’. Here are
some very important features to note about SQLite: self-contained, serverless, with
zero-configuration needed to run and transactional.

## PYTHON’S SQLITE MODULE
To allow us to use
SQLite with Python, the Python Standard Library includes a module called
"sqlite3".

```python
import​ sqlite3
```
We can then use the function ​ sqlite3.connect to connect to the database. We
pass the name of the database file to open or create it.

```python
# Creates or opens a file called student_db with a SQLite3 DB
db = sqlite3.connect(​ 'data/student_db'​ )
```

### Creating and Deleting Tables
To make any changes to the database, we need a ​ cursor object​ . A cursor object is
an object that is used to execute SQL statements. Next, ​ .commit ​ is used to save
changes to the database.

```python
cursor = db.cursor()
# Get a cursor object
cursor.execute(​ '''
CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT,
grade INTEGER)
'''​ )
db.commit()import​ sqlite3
```
### Inserting into the Database
To insert data, we use the cursor again to execute a SQL statement. When using
data stored in Python variables to insert data into a database table, use the "?"
placeholder. 

```python
cursor = db.cursor()
name1 = ​ 'Andres'
grade1 = ​ 60
name2 = ​ 'John'
grade2 = ​ 90
# Insert student 1
cursor.execute(​ '''INSERT INTO student(name, grade)
VALUES(?,?)'''​ , (name1,grade1))
print(​ 'First user inserted'​ )
# Insert student 2
cursor.execute(​ '''INSERT INTO student(name, grade)
VALUES(?,?)'''​ , (name2,grade2))
print(​ 'Second user inserted'​ )
db.commit()
```

### Retrieving Data
To retrieve data, execute a SELECT SQL statement against the cursor object and
then use ​ fetchone()​ to retrieve a single row or f
etchall()​ to retrieve all the rows.

```python
id = ​ 3
cursor.execute(​ '''SELECT name, grade FROM student
student = cursor.fetchone()
print(student)
WHERE id=?'''​ , (id,))
```
