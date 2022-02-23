sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'BLT', 'grilled cheese', 'pastrami']
finished_sandwiches = []

print("Sorry, we've run out of pastrami.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    # Skip pastrami sandwiches
    if current_sandwich == 'pastrami':
        continue
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print('\nSandwiches made:')
for sandwich in finished_sandwiches:
    print(sandwich)
