def count_names(filename):
    """Count the number of names in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass # Fail silently when a file is not found.
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} names.")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    count_names(filename)
