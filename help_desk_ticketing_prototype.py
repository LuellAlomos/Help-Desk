class Ticket:
    ticket_counter = 2000  # Initial ticket number

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def generate_password(self):
        if "Password Change" in self.description:
            new_password = f"{self.staff_id[:2]}{self.creator_name[:3]}"
            self.response = f"New password generated: {new_password}"

    def resolve_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def display_ticket(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")
        print("\n")


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def submit_ticket(self, staff_id, creator_name, contact_email, description):
        ticket = Ticket(staff_id, creator_name, contact_email, description)
        ticket.generate_password()
        self.tickets.append(ticket)
        return ticket

    def respond_to_ticket(self, ticket, response):
        ticket.response = response
        if "Password Change" in ticket.description or response.startswith("New password generated"):
            ticket.resolve_ticket()

    def reopen_ticket(self, ticket):
        ticket.reopen_ticket()

    def display_ticket_statistics(self):
        total_tickets = len(self.tickets)
        resolved_tickets = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in self.tickets if ticket.status == "Open")
        print(f"Tickets Created: {total_tickets}")
        print(f"Tickets Resolved: {resolved_tickets}")
        print(f"Tickets To Solve: {open_tickets}")
        print("\n")

    def display_all_tickets(self):
        for ticket in self.tickets:
            ticket.display_ticket()


# Main Program
if __name__ == "__main__":
    ticket_system = TicketingSystem()

    # Submitting tickets
    ticket1 = ticket_system.submit_ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = ticket_system.submit_ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = ticket_system.submit_ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password change")

    # Displaying ticket statistics
    ticket_system.display_ticket_statistics()

    # Responding to tickets
    ticket_system.respond_to_ticket(ticket1, "The monitor has been replaced.")
    ticket_system.respond_to_ticket(ticket3, "New password generated: JOJoh")

    # Displaying ticket information and statistics
    ticket_system.display_all_tickets()
    ticket_system.display_ticket_statistics()