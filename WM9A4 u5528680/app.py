# Import dependencies -- reuse code others have given us.
import sqlite3
import os
from markupsafe import escape
import datetime
from flask import Flask, render_template, request, url_for, redirect, abort, g

app = Flask(__name__)

# The database configuration
DATABASE = os.environ.get("FLASK_DATABASE", "app.db")


# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
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
def hello():
    """Return some friendly text."""
    return "Hello, Barbie"

### YOUR CODE GOES HERE ###
import getpass

# Dictionaries for storing data
users = {}  # username: password
orders = {}  # order_id: order_details
loyalty_points = {}  # username: points
coffee_shops = ["Café Library", "Pret A Manger", "Café Gibbet Hill", "Café Oculus",
                "Café Social", "Library Coffee Bar", "NAIC Café", "Red Rocket",
                "Aroma", "Caffè Nero", "University House Cafe", "WBS Café"]

# Coffee menus and waiting times for each shop
coffee_menus = {
    "Café Library": {"menu": ["Espresso", "Latte", "Cappuccino"], "wait_time": 5},
    "Pret A Manger": {"menu": ["Americano", "Flat White", "Mocha"], "wait_time": 7},
    # Add menus and waiting times for other coffee shops
}

def register():
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = getpass.getpass("Enter new password: ")
    users[username] = password
    loyalty_points[username] = 0
    print("Registration successful.")

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in users and users[username] == password:
        return username
    else:
        print("Invalid username or password.")
        return None

def select_coffee_shop():
    while True:
        print("Select a coffee shop:")
        for i, shop in enumerate(coffee_shops, 1):
            print(f"{i}. {shop}")
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(coffee_shops):
                chosen_shop = coffee_shops[choice - 1]
                print(f"You selected {chosen_shop}.")
                print("Menu:", ", ".join(coffee_menus[chosen_shop]["menu"]))
                print(f"Average waiting time: {coffee_menus[chosen_shop]['wait_time']} minutes.")
                return chosen_shop
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input, please enter a number.")

def create_order(user):
    shop = select_coffee_shop()
    coffee_type = input("Enter coffee type from the menu: ")
    size = input("Enter size: ")
    special_request = input("Any special requests? ")
    order_id = len(orders) + 1
    orders[order_id] = {"user": user, "coffee_shop": shop, "coffee_type": coffee_type, "size": size, "special_request": special_request}
    loyalty_points[user] += 10  # Add loyalty points
    print(f"Order created at {shop}. Your order ID is {order_id}.")

def view_orders(user):
    user_orders = [order for order_id, order in orders.items() if order["user"] == user]
    if not user_orders:
        print("No orders found.")
        return
    for order_id, order in orders.items():
        if order["user"] == user:
            print(f"Order ID: {order_id}, Coffee Shop: {order['coffee_shop']}, Coffee Type: {order['coffee_type']}, Size: {order['size']}, Special Request: {order['special_request']}")

def list_coffee_shops():
    print("\nList of Coffee Shops:")
    for shop in coffee_shops:
        print(f"- {shop}")

def main():
    while True:
        print("\nWelcome to Warwick Coffee Pre-Order System")
        print("1. Register")
        print("2. Login")
        print("3. List Coffee Shops")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Create Order")
                    print("2. View My Orders")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        create_order(user)
                    elif user_choice == "2":
                        view_orders(user)
                    elif user_choice == "3":
                        break
        elif choice == "3":
            list_coffee_shops()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    app.run(debug=True)