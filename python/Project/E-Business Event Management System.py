# Event Database
events = {}

# Event Management Functions
def create_event(event_id, name, date, speaker, capacity):
    events[event_id] = {'name': name, 'date': date, 'speaker': speaker, 'capacity': capacity, 'attendees': [], 'feedback': []}
    print(f"Event '{name}' created.")

def update_event(event_id, name, date, speaker, capacity):
    if event_id in events:
        events[event_id].update({'name': name, 'date': date, 'speaker': speaker, 'capacity': capacity})
        print(f"Event '{name}' updated.")
    else:
        print("Event not found.")

def register_for_event(event_id, user_name):
    if event_id in events and len(events[event_id]['attendees']) < events[event_id]['capacity']:
        events[event_id]['attendees'].append(user_name)
        print(f"{user_name} registered for event '{events[event_id]['name']}'.")
    else:
        print("Event not found or full.")

def display_event(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Speaker: {event['speaker']}, Capacity: {event['capacity']}, Attendees: {len(event['attendees'])}")
    else:
        print("Event not found.")

# Feedback Mechanism Functions
def collect_feedback(event_id, user_name, feedback):
    if event_id in events:
        events[event_id]['feedback'].append((user_name, feedback))
        print("Feedback collected.")
    else:
        print("Event not found.")

# Report Mechanism Functions
def generate_attendance_report(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"Attendance for '{event['name']}': {len(event['attendees'])} attendees.")
    else:
        print("Event not found.")

def generate_feedback_report(event_id):
    if event_id in events and events[event_id]['feedback']:
        print(f"Feedback for event '{events[event_id]['name']}':")
        for feedback in events[event_id]['feedback']:
            print(f"- {feedback[0]}: {feedback[1]}")
    else:
        print("Event not found or no feedback available.")

# User Interface Functions
def main_menu():
    while True:
        print("\nE-Business Event Management System\n")
        print("1. Create Event")
        print("2. Update Event")
        print("3. Register for Event")
        print("4. Display Event")
        print("5. Collect Feedback")
        print("6. Generate Attendance Report")
        print("7. Generate Feedback Report")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            event_id = input("Enter event ID: ")
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            speaker = input("Enter speaker name: ")
            capacity = int(input("Enter event capacity: "))
            create_event(event_id, name, date, speaker, capacity)
        elif choice == '2':
            event_id = input("Enter event ID: ")
            name = input("Enter new event name: ")
            date = input("Enter new event date: ")
            speaker = input("Enter new speaker name: ")
            capacity = int(input("Enter new event capacity: "))
            update_event(event_id, name, date, speaker, capacity)
        elif choice == '3':
            event_id = input("Enter event ID: ")
            user_name = input("Enter your name: ")
            register_for_event(event_id, user_name)
        elif choice == '4':
            event_id = input("Enter event ID: ")
            display_event(event_id)
        elif choice == '5':
            event_id = input("Enter event ID: ")
            user_name = input("Enter your name: ")
            feedback = input("Enter your feedback: ")
            collect_feedback(event_id, user_name, feedback)
        elif choice == '6':
            event_id = input("Enter event ID: ")
            generate_attendance_report(event_id)
        elif choice == '7':
            event_id = input("Enter event ID: ")
            generate_feedback_report(event_id)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

# Main Entry Point
if __name__ == "__main__":
    main_menu()
