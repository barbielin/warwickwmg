# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    if item in inventory:
        inventory[item]=inventory[item] + quantity #inventory[item] += quantity
    else:
        inventory[item]=quantity
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
    pass

# Function to view all items in the inventory
def view_inventory():
    for item,quantity in inventory. items():
        print(f"{item}:{quantity}")
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    pass

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    if item in inventory:
        inventory[item]= quantity
    else:
        print("not found in inventory")
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("Enter item:")
            try:
                quantity = int(input("Enter quantity:"))
            except:
                print("Error detected:please use number")
            add_item(item,quantity)
        elif choice == "2":
            item=input("Enter item:")
            view_inventory()
        elif choice == "3":
            item = input("Enter item:")
            quantity = int(input("Enter quantity:"))
            update_item(item,quantity)
        elif choice == "4":
            break
        else:
            print("Invalid input, try again")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()