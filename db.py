import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
sql_query = """CREATE TABLE passwords 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
password VARCHAR(255) NOT NULL)"""
cursor.execute(sql_query)

sql_query = """INSERT INTO passwords (id, password) VALUES ('1', 'AABCB')"""
cursor.execute(sql_query)
conn.commit()
conn.close()
