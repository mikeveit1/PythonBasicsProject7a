def count_letters(counted_string):
    """Takes as a parameter a string and returns a dictionary that tabulates how many
        of each letter is in that string."""
    letters = {}
    for letter in counted_string:
        letter = letter.upper()
        if 'A' <= letter <= 'Z':
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
    return letters
