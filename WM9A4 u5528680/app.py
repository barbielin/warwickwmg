# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from datetime import datetime
from flask import Flask, render_template, request, url_for, flash,redirect, g, session
app = Flask(__name__, template_folder='path/to/your/templates')

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
        student_id = request.form['student_id']
        password = request.form['psw']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute('SELECT password FROM users WHERE student_id = ?', (student_id,))
        user = cursor.fetchone()

        if user and user[0] == password:
            flash("Login successful.")
            return redirect(url_for('CoffeeShops'))
        else:
            flash("Invalid Student ID or password.")

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

@app.route('/CafeLibrary')
def CafeLibrary():
    return render_template('CafeLibrary.html')

@app.route('/orderform')
def orderform():
    return render_template('orderform.html')



# Route to display the order form
@app.route('/place_order', methods=['GET'])
def show_order_form():
    return render_template('order_form.html')

def predict_waiting_time(orders_ahead):
    average_prep_time = 5  # Average preparation time per order in minutes
    return average_prep_time * orders_ahead

# Route to handle form submission and store order in the database
@app.route('/place_order', methods=['POST'])
def place_order():
    student_id = request.form['student_id']
    coffee_type = request.form['coffee_type']
    quantity = request.form['quantity']
    if request.method == 'POST':
        # Check if it's a new day to reset orders_ahead
        current_date = datetime.now().date()
        last_order_date = session.get('last_order_date', None)
        if last_order_date is None or datetime.strptime(last_order_date, '%Y-%m-%d').date() < current_date:
            session['orders_ahead'] = 0  # Reset for a new day
            session['last_order_date'] = current_date.strftime('%Y-%m-%d')
        session['orders_ahead'] += 1  # Increment orders ahead for each order placed
        average_prep_time = 5  # Average preparation time per order in minutes
        waiting_time = session['orders_ahead'] * average_prep_time
        flash(f'Order placed successfully! Estimated waiting time is {waiting_time} minutes.')
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO CafeLibraryOrder (student_id, coffee_type, quantity) VALUES (?, ?, ?)',
                       (student_id, coffee_type, quantity))
        conn.commit()
    except sqlite3.Error as e:
        flash('Failed to place order: ' + str(e))
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('show_order'))

# Route to display the order history
@app.route('/show_order')
def show_order():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT student_id, coffee_type, quantity FROM CafeLibraryOrder')
        orders = cursor.fetchall()
    except sqlite3.Error as e:
        flash('Failed to retrieve order history: ' + str(e))
        orders = []
    finally:
        cursor.close()
        conn.close()

    return render_template('show_order.html', orders=orders)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)