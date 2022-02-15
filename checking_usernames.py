current_users = ['john', 'bob', 'mike', 'jane', 'jill']
new_users = ['john', 'jane', 'sarah', 'jim', 'joe']

for user in new_users:
    if user.lower() in current_users:
        print(f'{user} is already taken')
    else:
        print(f'{user} is available')
