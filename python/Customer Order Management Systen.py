# Customer and Product Databases
customers = {}
products = {}

# Customer Management Functions
def add_customer(id, name, contact):
    customers[id] = {'name': name, 'contact': contact, 'orders': []}
    print(f"Customer {name} added.")

def update_customer(id, name, contact):
    if id in customers:
        customers[id]['name'] = name
        customers[id]['contact'] = contact
        print(f"Customer {id} updated.")
    else:
        print(f"Customer {id} not found.")

def remove_customer(id):
    if id in customers:
        del customers[id]
        print(f"Customer {id} removed.")
    else:
        print(f"Customer {id} not found.")

def display_customer(id):
    if id in customers:
        customer = customers[id]
        print(f"Customer ID: {id}, Name: {customer['name']}, Contact: {customer['contact']}, Orders: {customer['orders']}")
    else:
        print(f"Customer {id} not found.")

# Product Management Functions
def add_product(id, name, price, quantity):
    products[id] = {'name': name, 'price': price, 'quantity': quantity}
    print(f"Product {name} added.")

def update_product(id, name, price, quantity):
    if id in products:
        products[id] = {'name': name, 'price': price, 'quantity': quantity}
        print(f"Product {id} updated.")
    else:
        print(f"Product {id} not found.")

def display_product(id):
    if id in products:
        product = products[id]
        print(f"Product ID: {id}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print(f"Product {id} not found.")

# Order Processing Functions
def add_product_to_order(customer_id, product_id):
    if customer_id in customers and product_id in products:
        if products[product_id]['quantity'] > 0:
            customers[customer_id]['orders'].append(products[product_id])
            update_stock(product_id, -1)
            print(f"Product {product_id} added to customer {customer_id}'s order.")
        else:
            print(f"Product {product_id} is out of stock.")
    else:
        print(f"Invalid customer ID or product ID.")

def calculate_order_total(customer_id):
    if customer_id in customers:
        total = sum(product['price'] for product in customers[customer_id]['orders'])
        print(f"Total order cost for customer {customer_id} is ${total:.2f}")
        return total
    else:
        print(f"Customer {customer_id} not found.")
        return 0

def update_stock(product_id, change):
    if product_id in products and (products[product_id]['quantity'] + change) >= 0:
        products[product_id]['quantity'] += change
    else:
        print(f"Invalid stock update for product {product_id}.")

# Reporting System
def total_sales_report():
    total_sales = sum(product['price'] for product in products.values())
    print(f"Total sales: ${total_sales:.2f}")

def popular_products_report():
    # Placeholder for simplicity, as this requires more complex data analysis
    print("Most popular products report is currently unavailable.")

def customer_order_history_report(customer_id):
    if customer_id in customers:
        orders = customers[customer_id]['orders']
        if orders:
            print(f"Order history for customer {customer_id}:")
            for order in orders:
                print(order)
        else:
            print(f"No orders for customer {customer_id}.")
    else:
        print(f"Customer {customer_id} not found.")

# User Interface Functions
def main_menu():
    while True:
        print("\nCustomer Order Management System\n")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Remove Customer")
        print("4. Display Customer")
        print("5. Add Product")
        print("6. Update Product")
        print("7. Display Product")
        print("8. Add Product to Order")
        print("9. Calculate Order Total")
        print("10. Total Sales Report")
        print("11. Popular Products Report")
        print("12. Customer Order History Report")
        print("13. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            contact = input("Enter customer contact: ")
            add_customer(id, name, contact)
        elif choice == '2':
            id = input("Enter customer ID: ")
            name = input("Enter new name: ")
            contact = input("Enter new contact: ")
            update_customer(id, name, contact)
        elif choice == '3':
            id = input("Enter customer ID: ")
            remove_customer(id)
        elif choice == '4':
            id = input("Enter customer ID: ")
            display_customer(id)
        elif choice == '5':
            id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(id, name, price, quantity)
        elif choice == '6':
            id = input("Enter product ID: ")
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            quantity = int(input("Enter new product quantity: "))
            update_product(id, name, price, quantity)
        elif choice == '7':
            id = input("Enter product ID: ")
            display_product(id)
        elif choice == '8':
            customer_id = input("Enter customer ID: ")
            product_id = input("Enter product ID: ")
            add_product_to_order(customer_id, product_id)
        elif choice == '9':
            customer_id = input("Enter customer ID: ")
            calculate_order_total(customer_id)
        elif choice == '10':
            total_sales_report()
        elif choice == '11':
            popular_products_report()
        elif choice == '12':
            customer_id = input("Enter customer ID: ")
            customer_order_history_report(customer_id)
        elif choice == '13':
            break
        else:
            print("Invalid choice. Please try again.")

# Main Entry Point
if __name__ == "__main__":
    main_menu()
