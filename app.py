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
         msg= None
         try:
            post_data = request.get_json()
            name = post_data['name']
            surname = post_data['surname']
            email = post_data['email']
            username = post_data['username']
            password = post_data['password']

            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                conn.row_factory = dict_factory
                cur.execute("INSERT INTO user(name, surname, email, username, password) VALUES(?,?,?,?,?)", (name, surname, email, username, password))
                conn.commit()
                msg = "Record added successfully"

         except Exception as e:
            msg = 'error'+ str(e)

         finally:
            return {'msg': msg}
# @app.route('/list-users/', methods=['GET'])
# # def list():
# #     try:
# #         with sqlite3.connect('database.db') as conn:
# #                 cur = conn.cursor()
# #                 conn.row_factory = dict_factory
# #                 cur.execute("SELECT * FROM users")
# #                 print(cur.fetchall())
# #     except Exception as e:
# #         conn.rollback()
# #         response
