from fastapi import FastAPI, Request
import sqlite3

app = FastAPI()

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('passwords.db')
    except sqlite3.Error as e:
        print(e)

    return conn


@app.post("/")
def unlock(password: str):
    conn = db_connection()
    cursor = conn.cursor()
    sql_query = f"SELECT password FROM passwords WHERE password='{password}'"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    
    user_pass = None
    for row in rows:
        user_pass = row
        
    if user_pass:
        return "User Authorized!"
    
    return "Unauthorized!"