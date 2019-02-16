#!/usr/bin/env python
from sys import argv
from unicodedata import normalize

def clean(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

def char_count(txt):
    # Builds a dictionary with the number of chars in the word
    chars = list(txt) # a list of all chars in the word
    cdict = {}
    for c in chars:
        if c not in cdict:
            cdict[c] = 1
        else:
            cdict[c] = cdict[c] + 1
    return cdict

def perm(dict_file, search, fixed_len=-1):
    # Build dictionary of chars of the search word
    search_dict = char_count(search)
    # Makes search lowercase
    search = search.lower()
    
    # Reads all words in dictionary and change them to lowercase
    print("Trying to open dictionary file ({})... ".format(dict_file))
    try:
        f = open(dict_file, 'r')
    except IOError as err:
        return "{0}".format(err.strerror)

    print('Success!')

    # Builds dictionary for each word and compares with searched-word dictionary
    results = []
    for line in f:
        word = clean(line.rstrip().lower())
        word_dict = char_count(word)

        if (fixed_len == -1) or (fixed_len > 0 and len(word) == int(fixed_len)):

            # Comparison
            word_in_search = True
            for key in word_dict.keys():
                if key in search_dict.keys():
                    if word_dict[key] > search_dict[key]:
                        word_in_search = False
                        break
                else:
                    word_in_search = False
                    break
        
            if (word_in_search) and (word not in results):
                results.append(word)

    f.close
    return 'Valid word: {}'.format(', '.join(results))

def main():
    if len(argv) == 4:
        print(perm(argv[1], argv[2], argv[3]))
    elif len(argv) == 3:
        print(perm(argv[1], argv[2]))
    else:
        print("Usage: scrabble.py [DICTIONARY FILE] [WORD] [OPTIONAL: LENGTH]")

if __name__ == '__main__':
    main()
