def count_occurences(filename, word):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass # Fail silently when a file is not found.
    else:
        num_occurences = contents.lower().count(word)
        print(f"The file {filename} has {num_occurences} occurences of '{word}'.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_women.txt']

word = 'the'
for filename in filenames:
    count_occurences(filename, word)
