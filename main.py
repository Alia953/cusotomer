# main.py
from ticket_manager import create_ticket, view_tickets, resolve_ticket

def display_menu():
    print("\nCustomer Support System")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Mark a ticket as resolved")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter your name: ")
            issue = input("Describe your issue: ")
            create_ticket(name, issue)
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            ticket_id = int(input("Enter the ticket ID to mark as resolved: "))
            resolve_ticket(ticket_id)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
