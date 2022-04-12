from random import choice

possibilities = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

def generate_random_ticket():
    """"Generates a ticket for the lottery."""
    generated_ticket = []
    for i in range(4):
        generated_ticket.append(choice(possibilities))
    return generated_ticket

def check_ticket(winning_ticket, ticket):
    """"Checks the ticket for the lottery."""
    for element in ticket:
        if element not in winning_ticket:
            return False

    return true

winning_ticket = generate_random_ticket()

print("Welcome to the lottery!")
print(f"Any ticket matching this wins a prize: \
{winning_ticket}")

ticket_count = 0

while generate_random_ticket() != winning_ticket:
    ticket_count += 1

print(f"It took {ticket_count} tickets to win the lottery.")
