languages = ['english', 'mandarin', 'spanish', 'french', 'german']

print('\nLanguages:')
print(languages)

languages.append('italian')
print('\nLanguages after appending "italian":')
print(languages)

languages.insert(0, 'japanese')
print('\nLanguages after inserting "japanese" at index 0:')
print(languages)

del languages[1]
print('\nLanguages after deleting the second element:')
print(languages)

popped_language = languages.pop()
print(f'\nLanguages after popping "{popped_language}":')
print(languages)

languages.remove('japanese')
print('\nLanguages after removing "japanese":')
print(languages)

languages.sort()
print('\nLanguages after sorting:')
print(languages)

languages.sort(reverse = True)
print('\nLanguages after sorting in reverse order:')
print(languages)

print('\nLanguages after temporarily sorting:')
print(sorted(languages))

languages.reverse()
print('\nLanguages after reversing:')
print(languages)

languages_length = len(languages)
print(f'\nThere are {languages_length} languages in the list.')