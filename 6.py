# Simple Help Desk Expert System
tickets = {}
solutions = {
    "password": "Reset at: booking.com/reset",
    "email": "Check email.booking.com/status",
    "login": "Try forgot password option",
    "printer": "Restart printer and computer"
}

while True:
    print("\n1. New Ticket 2. View Ticket 3. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Your name: ")
        issue = input("Issue: ")
        ticket_id = len(tickets) + 100
        tickets[ticket_id] = {
            "name": name,
            "issue": issue,
            "solution": solutions.get(issue.lower(), "We'll contact you")
        }
        print(f"Ticket #{ticket_id} created!")
        print("Try:", tickets[ticket_id]["solution"])
    
    elif choice == "2":
        ticket_id = int(input("Ticket #: "))
        if ticket_id in tickets:
            print(f"\n{tickets[ticket_id]['name']}'s issue:")
            print("Problem:", tickets[ticket_id]["issue"])
            print("Solution:", tickets[ticket_id]["solution"])
        else:
            print("Ticket not found")
    
    elif choice == "3":
        print("Goodbye!")
        break