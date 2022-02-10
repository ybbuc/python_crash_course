locations = ['paris', 'berlin', 'los angeles', 'sao paulo', 'cairo']

print('\nLocations in original order:')
print(locations)

print('\nLocations in alphabetical order:')
print(sorted(locations))

print('\nLocations in original order:')
print(locations)

print('\nLocations in reverse alphabetical order:')
print(sorted(locations, reverse=True))

print('\nLocations in original order:')
print(locations)

print('\nLocations in reverse order:')
locations.reverse()
print(locations)

print('\nLocations in alphabetical order:')
locations.sort()
print(sorted(locations))

print('\nLocations in reverse alphabetical order:')
locations.sort(reverse=True)
print(locations)