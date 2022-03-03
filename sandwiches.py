def make_sandwich(*ingredients):
    print('\nMaking a sandwich with the following ingredients:')
    for ingredient in ingredients:
        print('- ' + ingredient)

make_sandwich('turkey', 'cheese', 'lettuce', 'tomato')

make_sandwich('bacon', 'lettuce', 'tomato')
