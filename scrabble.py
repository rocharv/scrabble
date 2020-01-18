#!/usr/bin/python3
from sys import argv
from unicodedata import category, normalize


def strip_accents(s):
    """Return a string identical to s, but removing its accents."""
    return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')


def char_count(word):
    """Return a dictionary with the incidence of each character."""
    rdict = {}
    chars = list(word) # turn string into list
    for c in chars:
            if c in rdict:
                rdict[c] += 1
            else:
                rdict[c] = 1
    return rdict


def scrabble(dict_file_name, word, word_len = -1):
    result = [] # returned word list

    # Parameter confirmation message
    print("Available letters: {}".format(word))
    if word_len != -1:
        print("Searching words with {} letter(s).".format(word_len))

    # Try to open dictionary file
    try:
        print("Trying to open dictionary file ({})... ".format(dict_file_name))
        dict_file = open(dict_file_name, "rt")
    except IOError as err:
        return "{0}".format(err.strerror)
    print("Success!")

    # Build char_count dictionary for the provided word
    wcount = char_count(strip_accents(word))

    # Go through each line in the file searching for matching words
    for line in dict_file:
        line_word = line.rstrip().lower()
        no_accents_line_word = strip_accents(line_word)
        # Build char_count dictionary for the word in the current line
        lcount = char_count(no_accents_line_word)
        # Go through each character in the word line
        word_match = True
        for lkey in lcount.keys():
            if lkey not in wcount.keys() or wcount[lkey] < lcount[lkey]:
                word_match = False
                break
        # Append word in line in case of match
        if word_match and (word_len == -1 or len(line_word) == int(word_len)):
            result.append(line_word)

    print("Valid words: {}".format(', '.join(result)))


if __name__ == "__main__":
    if len(argv) == 4:
        scrabble(argv[1], argv[2], argv[3])
    elif len(argv) == 3:
        scrabble(argv[1], argv[2])
    else:
        print("Usage: scrabble.py [DICTIONARY FILE] [WORD] [OPTIONAL: LENGTH]")
