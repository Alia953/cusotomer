# data_store.py

# A list to store tickets
tickets = []

# Function to add a ticket to the list
def add_ticket(ticket):
    tickets.append(ticket)

# Function to get all tickets
def get_all_tickets():
    return tickets

# Function to mark a ticket as resolved by its ID
def mark_ticket_resolved(ticket_id):
    for ticket in tickets:
        if ticket['id'] == ticket_id:
            ticket['status'] = 'Resolved'
            break
