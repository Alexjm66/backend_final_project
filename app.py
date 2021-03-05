from flask import Flask,request,jsonify
import sqlite3
from flask_cors import CORS

def init_sqlite_db():

    con = sqlite3.connect('database.db')
    print("Created Database successfully")

    con.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, email TEXT, username TEXT, password TEXT)')
    print("Users Table created successfully")

    con.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, brand TEXT, image TEXT)')
    print("Products table created successfully")

    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM users")
    print(mycursor.fetchall())

    con.close()

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
                cur.execute("INSERT INTO users(name, surname, email, username, password) VALUES(?,?,?,?,?)", (name, surname, email, username, password))
                conn.commit()
                msg = "Record added successfully"

         except Exception as e:
            msg = 'error'+ str(e)

         finally:
            return {'msg': msg}

@app.route('/list-users/', methods=['GET'])
def list():
    try:
        with sqlite3.connect('database.db') as conn:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                cur.execute("SELECT * FROM users")
                rows = cur.fetchall()
    except Exception as e:
        print("Something went wrong" + str(e))
    return jsonify(rows)

# @app.route('/add-products', methods=['POST'])
# def add_prod():
#
#     with sqlite3.connect('database.db') as conn:
#             cur = conn.cursor()
#             conn.row_factory = dict_factory
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)",('Air force 1 Foamposite', 'Mens Shoe', 'R 3000', 'Nike', 'https://i.postimg.cc/gJJyBxCv/image1.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Addidas Vegeta', 'Mens Shoe', 'R 2800', 'Addidas', 'https://i.postimg.cc/v8CjfynP/image2.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Air jordan 1 ', 'Mens Shoe', 'R 2100', 'Nike', 'https://i.postimg.cc/j5b6t8n4/img02-removebg-preview-1.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Air max 97', 'Mens Shoe', 'R 2100', 'Nike', 'https://i.postimg.cc/434FsxC3/image3.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Jordan 11', 'Womens Shoe', 'R 3800', 'Jordan', 'https://i.postimg.cc/c1T7GBxf/img03-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Jordan 11 Gamma Blue', 'Mens Shoe', 'R 3200', 'Jordan', 'https://i.postimg.cc/13svr33K/image4.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Jordan Retro 6 ', 'Womens Shoe', 'R 2800', 'Jordan', 'https://i.postimg.cc/BQ6TSPbk/img04-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Cmft Air max 10', 'Mens Shoe', 'R 3800', 'Jordan', 'https://i.postimg.cc/wMDkDCKP/image5.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Air max 97', 'Womens Shoe', 'R 2800', 'Jordan', 'https://i.postimg.cc/bwS1bXQR/img06-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Jordan 3lab5', 'Mens Shoe', 'R 4200', 'Jordan', 'https://i.postimg.cc/PfDKGwL4/image6.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Jordan Retro 14', 'Mens Shoe', 'R 3100', 'Jordan', 'https://i.postimg.cc/MZsBFZ5D/img08-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air Uptempo 94', 'Mens Shoe', 'R 2800', 'Nike', 'https://i.postimg.cc/9Fr953Nj/img12-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air Uptempo Teardrop', 'Mens Shoe', 'R 3200', 'Nike', 'https://i.postimg.cc/bvjStZYz/img13-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Shox BB4', 'Mens Shoe', 'R 4200', 'Nike', 'https://i.postimg.cc/wTC7C1mh/img14-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike CB 94', 'Mens Shoe', 'R 3200', 'Nike', 'https://i.postimg.cc/50KtnyJQ/img18-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Airmore Uptempo', 'Womens Shoe', 'R 3200', 'Nike', 'https://i.postimg.cc/bwTHqXjY/download-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air max 98', 'Womens Shoe', 'R 2800', 'Nike', 'https://i.postimg.cc/SKR8qJrV/img01-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air Max Tailwind', 'Womens Shoe', 'R 2200', 'Nike', 'https://i.postimg.cc/0yBjYZYd/images-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air max 97', 'Womens Shoe', 'R 2700', 'Nike', 'https://i.postimg.cc/qRf7YRZN/Nike-Air-Max-97-Summit-White-Bleached-Coral-W-Product-removebg-preview.png'))
#             cur.execute("INSERT INTO products(name, description, price, brand, image) VALUES (?, ?, ?, ?, ?)", ('Nike Air max 98', 'Womens Shoe', 'R 2800', 'Nike', 'https://i.postimg.cc/cC0LxzWZ/nike-air-max-98-white-640744-106-620x-removebg-preview.png'))
#             conn.commit()
#
# add_prod()


@app.route('/list-prod/', methods=['GET'])
def list_prod():
    data = []
    try:
        with sqlite3.connect('database.db') as conn:
                conn.row_factory = dict_factory
                cur = conn.cursor()
                cur.execute("SELECT * FROM products")
                data = cur.fetchall()
    except Exception as e:
        conn.rollback()
        print("Something went wrong" + str(e))
    finally:
        conn.close()
        return jsonify(data)
