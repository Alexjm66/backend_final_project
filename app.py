from flask import Flask,request,jsonify
import sqlite3
from flask_cors import CORS

def init_sqlite_db():

    con = sqlite3.connect('database.db')
    print("Created Database successfully")

    con.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, email TEXT, username TEXT, password TEXT)')
    print("Table created successfully")

init_sqlite_db()

app = Flask (__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
@app.route('/add_new_user/', methods=['POST'])
def add_new_user():
     if request.method == "POST":
        msg = None
        try:
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                conn.row_factory = dict_factory
                cur.execute("INSERT INTO user(name, surname, email, username, password) VALUES(?,?,?,?,?)", (name, surname, email, username, password))
                conn.commit()
                msg = name + "was successfully added to the database"
        except Exception as e:
            conn.rollback()
            msg = "Error occurred in insert operation: " + str(e)

        finally:
            conn.close()
            return jsonify(msg)
