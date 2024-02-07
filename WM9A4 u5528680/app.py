# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, flash,redirect, g, session

app = Flask(__name__)
app.secret_key='your_secret_key'

# The database configuration
DATABASE_PATH = os.environ.get("FLASK_DATABASE", "pma_CoffeeOrder.db")
DATABASE = os.path.join(os.getcwd(),DATABASE_PATH)

# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# Each @app.route(...) indicates a URL.
# Using that URL causes the function immediately after the @app.route(...) line to run.
# THIS ROUTE IS TO PROVE THE FLASK SETUP WORKS.
# YOU SHOULD REPLACE IT WITH YOUR OWN CONTENT.
@app.route("/")
def Hello():
    """Return some friendly text."""
    return "Hi"

@app.route("/Contact")
def Contact():
    """Return some friendly text."""
    return "Hello, Barbie"

### YOUR CODE GOES HERE ###
import getpass
# Dictionaries for storing data
users = {}  # username: password

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['Username']
        student_id = request.form['Student ID']
        password = request.form['psw']
        repeat_password = request.form['psw-repeat']

        if password != repeat_password:
            flash("Registration error. Passwords do not match.")
            return redirect(url_for('register'))

        db = get_db_connection()
        cursor = db.cursor()

        try:
            cursor.execute('INSERT INTO users (email, username, student_id, password, repeat_password) VALUES (?, ?, ?, ?, ?)', 
                           (email, username, student_id, password, repeat_password))
            db.commit()
            flash("Registration successful. Please login.")
            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            flash("Registration error. Email already used.")
            return redirect(url_for('register'))
        finally:
            cursor.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute('SELECT password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()

        if user and user[0] == password:
            flash("Login successful.")
            return redirect(url_for('CoffeeShops'))
        else:
            flash("Invalid email or password.")

        cursor.close()

    return render_template('login.html')

@app.route('/CoffeeShops')
def CoffeeShops():
    return render_template('CoffeeShops.html')

def init_db():
    with app.app_context():
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                student_id TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        db.commit()

@app.route('/Café Library')
def CaféLibrary():
    return render_template('Café Library.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    name = request.form['name']
    coffee_type = request.form['coffee_type']
    quantity = request.form['quantity']
    
    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute('INSERT INTO orders (name, coffee_type, quantity) VALUES (?, ?, ?)',
                       (name, coffee_type, quantity))
        db.commit()
        flash('Order placed successfully!')
    except sqlite3.Error as e:
        flash('There was an issue placing your order: ' + str(e))
    finally:
        cursor.close()
        db.close()

    # Redirect to a new page or back to the form page after order placement
    return redirect(url_for('order_form'))

@app.route('/order', methods=['GET'])
def order_form():
    # Render your order form page here
    return render_template('order.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)