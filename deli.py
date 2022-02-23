sandwich_orders = ['pastrami', 'tuna', 'BLT', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print('\nSandwiches made:')
for sandwich in finished_sandwiches:
    print(sandwich)
