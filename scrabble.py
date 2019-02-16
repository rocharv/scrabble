#!/usr/bin/env python
import itertools
import sys

def permutations(dic_file, search, fixed_len):
    # Makes search lowercase
    search = search.lower()
    
    try:
        # Reads all words in dictionary and turn them lowercase
        dic = []
        print("Trying to open dictionary file ({})... ".format(dic_file))
        f = open(dic_file, 'r')
        for line in f:
            dic.append(line.rstrip().lower())
        f.close
        print('Dictionary successfully loaded: {} words were found.'.format(len(dic)))

        # Finds all permutations of searched word
        s = []
        
        if fixed_len > 0:
            s1 = itertools.permutations(search, int(fixed_len))
            for c in s1:
                s.append(''.join(c))
        else:
            for i in range(1,len(search)+1):
                s1 = itertools.permutations(search, i)
                for c in s1:
                    s.append(''.join(c))

        s = list(dict.fromkeys(s))

        # Finds all permutation of searched word
        found_words = []
        for w in dic:
            if w in s:
                found_words.append(w)
        return 'Valid words: {}'.format(', '.join(found_words))

    except IOError as err:
       print("{0}".format(err.strerror)) 

def main():
    if len(sys.argv) == 4:
        print(permutations(sys.argv[1], sys.argv[2], sys.argv[3]))
    else:
        if len(sys.argv) == 3:
            print(permutations(sys.argv[1], sys.argv[2], -1))
        else:
            print("Usage: scrabble.py [DICTIONARY FILE] [WORD] [OPTIONAL: LENGTH]")

if __name__ == '__main__':
    main()
