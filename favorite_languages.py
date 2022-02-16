favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
