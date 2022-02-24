def submit(filename, ingredients):
    with open(filename, 'w') as f:
        f.write(str(len(ingredients)) + ' ')
        f.write(' '.join(ingredients))
        