Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.chdir(r'C:\Users\pratik\OneDrive\Documents\CPA\PYTHON\BATCH_CODES\BATCH_46\SESSION_110\')
         
SyntaxError: unterminated string literal (detected at line 1)
path_name = r'C:\Users\pratik\OneDrive\Documents\CPA\PYTHON\BATCH_CODES\BATCH_46\SESSION_110'
         
os.chdir(path_name)
         
os.getcwd()
         
'C:\\Users\\pratik\\OneDrive\\Documents\\CPA\\PYTHON\\BATCH_CODES\\BATCH_46\\SESSION_110'
db_file_name = 'PyStudent.db'
         
import sqlite3
         
conn = sqlite3.connect(db_file_name)
         
type(conn)
         
<class 'sqlite3.Connection'>
curs = conn.cursor()
         
type(curs)
         
<class 'sqlite3.Cursor'>
create_query = 'create table PyStudent (st_id integer primary key, st_name text, st_city text, st_marks float)'
         
curs.execute(create_query)
         
<sqlite3.Cursor object at 0x000002B693C5B4C0>
curs.execute(create_query)
         
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    curs.execute(create_query)
sqlite3.OperationalError: table PyStudent already exists
insert_query = 'insert into PyStudent (st_id, st_name, st_city, st_marks) values(1, "Yogeshwar", "Pune", 80.5)'
         
curs.execute(insert_query)
         
<sqlite3.Cursor object at 0x000002B693C5B4C0>
curs.execute(insert_query)
         
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    curs.execute(insert_query)
sqlite3.IntegrityError: UNIQUE constraint failed: PyStudent.st_id
curs.rowcount
         
-1
st=(2, 'Radhika', 'Mumbai', 80.80)
curs.execute('insert into PyStudent values(?, ?, ?, ?)', st)
<sqlite3.Cursor object at 0x000002B693C5B4C0>
st_rolls, st_names, st_city, st_marks = [3, 4, 5, 6], ['Amit', 'Imran', 'Yogita', 'Tejas'], ['Pune', 'Pune', 'Mumbai', 'Mumbai'], [80.54, 79.54, 85.63, 83.23]
for t in zip(st_rolls, st_names, st_city, st_marks):
    print(t)

    
(3, 'Amit', 'Pune', 80.54)
(4, 'Imran', 'Pune', 79.54)
(5, 'Yogita', 'Mumbai', 85.63)
(6, 'Tejas', 'Mumbai', 83.23)
for student in zip(st_rolls, st_names, st_city, st_marks):
    curs.execute('insert into PyStudent (?, ?, ?, ?)', student)

         
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    curs.execute('insert into PyStudent (?, ?, ?, ?)', student)
sqlite3.OperationalError: near "?": syntax error
for student in zip(st_rolls, st_names, st_city, st_marks):
    curs.execute('insert into PyStudent values(?, ?, ?, ?)', student)

         
<sqlite3.Cursor object at 0x000002B693C5B4C0>
<sqlite3.Cursor object at 0x000002B693C5B4C0>
<sqlite3.Cursor object at 0x000002B693C5B4C0>
<sqlite3.Cursor object at 0x000002B693C5B4C0>
curs.rowcount
         
1
st_rolls, st_names, st_city, st_marks = [7, 8, 9, 10], ['Ravindra', 'Mayuresh', 'Rushikesh', 'Nateshwar'], ['Pune', 'Pune', 'Mumbai', 'Mumbai'], [82.54, 69.54, 90.63, 92.23]
         
student_list = []
         
for student in zip(st_rolls, st_names, st_city, st_marks):
         student_list.append(student)

         
student_list
         
[(7, 'Ravindra', 'Pune', 82.54), (8, 'Mayuresh', 'Pune', 69.54), (9, 'Rushikesh', 'Mumbai', 90.63), (10, 'Nateshwar', 'Mumbai', 92.23)]
curs.executemany('insert into PyStudent values(?,?,?,?)', student_list)
         
<sqlite3.Cursor object at 0x000002B693C5B4C0>
curs.rowcount
         
4
conn.commit()
         
