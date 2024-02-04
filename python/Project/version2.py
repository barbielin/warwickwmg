# Event Database
events = {}

# Customer Database
customers = {}

# Event Management Functions
def create_event(event_id, name, date, speaker, capacity, address):
    events[event_id] = {'name': name, 'date': date, 'speaker': speaker, 'capacity': capacity, 'address': address, 'attendees': [], 'feedback': []}
    print(f"Event '{name}' created.")

def update_event(event_id, name, date, speaker, capacity, address):
    if event_id in events:
        events[event_id].update({'name': name, 'date': date, 'speaker': speaker, 'capacity': capacity, 'address': address})
        print(f"Event '{name}' updated.")
    else:
        print("Event not found.")

def display_event(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Speaker: {event['speaker']}, Capacity: {event['capacity']}, Address: {event['address']}, Attendees: {len(event['attendees'])}")
    else:
        print("Event not found.")


# Customer Management Functions
def add_customer(customer_id, name, email):
    customers[customer_id] = {'name': name, 'email': email, 'loyalty_points': 0}
    print(f"Customer '{name}' added.")

def display_customer_list():
    if customers:
        for customer_id, info in customers.items():
            print(f"Customer ID: {customer_id}, Name: {info['name']}, Email: {info['email']}, Loyalty Points: {info['loyalty_points']}")
    else:
        print("No customers available.")

def update_loyalty_points(customer_id, points):
    if customer_id in customers:
        customers[customer_id]['loyalty_points'] += points
        print(f"{points} loyalty points added to customer {customer_id}.")
    else:
        print("Customer not found.")

def register_for_event(event_id, customer_id):
    if event_id in events and customer_id in customers:
        if len(events[event_id]['attendees']) < events[event_id]['capacity']:
            events[event_id]['attendees'].append(customer_id)
            update_loyalty_points(customer_id, 10)  # Assume 10 points per event registration
            print(f"Customer {customer_id} registered for event '{events[event_id]['name']}'.")
        else:
            print("Event is full.")
    else:
        print("Event or customer not found.")

# Feedback Mechanism Functions
def collect_feedback(event_id, customer_id, feedback):
    if event_id in events and customer_id in customers:
        events[event_id]['feedback'].append((customer_id, feedback))
        print("Feedback collected.")
    else:
        print("Event or customer not found.")

# Report Mechanism Functions
def generate_attendance_and_customer_report():
    for event_id, event in events.items():
        print(f"\nEvent: {event['name']} - Date: {event['date']}")
        if event['attendees']:
            for attendee in event['attendees']:
                if attendee in customers:
                    customer = customers[attendee]
                    print(f"Customer ID: {attendee}, Name: {customer['name']}, Loyalty Points: {customer['loyalty_points']}")
                else:
                    print(f"Attendee (ID: {attendee}) not found in customer database.")
        else:
            print("No attendees for this event.")

def generate_feedback_report(event_id):
    if event_id in events and events[event_id]['feedback']:
        print(f"Feedback for event '{events[event_id]['name']}':")
        for feedback in events[event_id]['feedback']:
            print(f"- Customer ID {feedback[0]}: {feedback[1]}")
    else:
        print("Event not found or no feedback available.")

# User Interface Functions
def main_menu():
    while True:
        print("\nE-Business Event Management System\n")
        print("1. Create Event")
        print("2. Edit Event")
        print("3. Display Event")
        print("4. Add Customer")
        print("5. Customer List")
        print("6. Generate Attendance and Customer Detail Report")
        print("7. Generate Feedback Report")
        print("8. Register Here")
        print("9. Provide Feedback")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            event_id = input("Enter event ID: ")
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            speaker = input("Enter speaker name: ")
            capacity = int(input("Enter event capacity: "))
            address = input("Enter event address: ")
            create_event(event_id, name, date, speaker, capacity, address)
        elif choice == '2':
            event_id = input("Enter event ID: ")
            name = input("Enter new event name: ")
            date = input("Enter new event date: ")
            speaker = input("Enter new speaker name: ")
            capacity = int(input("Enter new event capacity: "))
            address = input("Enter new event address: ")
            update_event(event_id, name, date, speaker, capacity, address)
        elif choice == '3':
            event_id = input("Enter event ID: ")
            display_event(event_id)
        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            add_customer(customer_id, name, email)
        elif choice == '5':
            display_customer_list()
        elif choice == '6':
            generate_attendance_and_customer_report()
        elif choice == '7':
            event_id = input("Enter event ID for feedback report: ")
            generate_feedback_report(event_id)
        elif choice == '8':
            event_id = input("Enter event ID to register: ")
            customer_id = input("Enter your customer ID: ")
            register_for_event(event_id, customer_id)
        elif choice == '9':
            event_id = input("Enter event ID: ")
            customer_id = input("Enter your customer ID: ")
            feedback = input("Enter your feedback: ")
            collect_feedback(event_id, customer_id, feedback)
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

# Main Entry Point
if __name__ == "__main__":
    main_menu()
