# customer_support_system_gui.py
# Single-file Customer Support System with Tkinter GUI
# Uses only built-in Python libraries

import tkinter as tk
from tkinter import messagebox

# -------------------------
# In-memory Data Store
# -------------------------
tickets = []
ticket_counter = 1


# -------------------------
# Ticket Manager Functions
# -------------------------
def create_ticket(name, issue):
    """Create and store a new support ticket."""
    global ticket_counter
    ticket = {
        "id": ticket_counter,
        "name": name,
        "issue": issue,
        "status": "Open"
    }
    tickets.append(ticket)
    ticket_counter += 1
    return ticket


def view_tickets():
    """Return all tickets."""
    return tickets


def resolve_ticket(ticket_id):
    """Resolve a ticket by ID."""
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            if ticket["status"] == "Resolved":
                return False
            ticket["status"] = "Resolved"
            return True
    return None


# -------------------------
# GUI Application
# -------------------------
class SupportSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Support System")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # --- Create Ticket Section ---
        tk.Label(root, text="Customer Name:", font=("Arial", 11, "bold")).pack(pady=2)
        self.entry_name = tk.Entry(root, width=45)
        self.entry_name.pack()

        tk.Label(root, text="Issue Description:", font=("Arial", 11, "bold")).pack(pady=2)
        self.entry_issue = tk.Entry(root, width=45)
        self.entry_issue.pack()

        tk.Button(root, text="Create Ticket", bg="lightgreen",
                  command=self.create_ticket).pack(pady=5)

        # --- View Tickets Section ---
        tk.Button(root, text="View All Tickets", bg="lightblue",
                  command=self.view_tickets).pack(pady=5)

        # --- Resolve Ticket Section ---
        tk.Label(root, text="Ticket ID to Resolve:", font=("Arial", 11, "bold")).pack(pady=2)
        self.entry_ticket_id = tk.Entry(root, width=15)
        self.entry_ticket_id.pack()
        tk.Button(root, text="Resolve Ticket", bg="orange",
                  command=self.resolve_ticket).pack(pady=5)

        # --- Output Display Area ---
        self.output_area = tk.Text(root, height=15, width=70, wrap="word")
        self.output_area.pack(pady=10)

    # -------------------------
    # GUI Methods
    # -------
