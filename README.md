# Scrabble
A simple scrabble helper in Python.

# Usage
./scrabble.py [DICTIONARY FILE] [WORD] [OPTIONAL: LENGTH]

For instance, if you type on a terminal:
			
    ./scrabble.py en-us.txt brain
	
The output is going to be:

    Trying to open dictionary file (en-us.txt)...
    Dictionary successfully loaded: 466544 words were found.
    Valid words: a, ab, abi, abir, abn, abr, abri, abrin, ai, ain, air, airn, an, ani, ar, arb, ari, arin, arn, arni, b, ba, bai, bain, bairn, ban, bani, bar, bari, barn, bi, bia, bin, bina, birn, bn, br, bra, brain, bran, bri, bria, brian, brin, brina, brn, i, ia, iab, ian, ib, iba, iban, ibn, in, ina, ir, ira, iran, irn, n, na, nab, naib, nair, nar, nari, nb, nba, ni, nia, nib, nir, nira, nr, nra, nrab, r, ra, rab, rabi, rabin, rai, rain, ran, rani, rb, rbi, ri, ria, rib, riba, rin, rina, rn, rna

You also can specify the length of the output words:

    ./scrabble.py en-us.txt brain 5

This will result in:

    Trying to open dictionary file (en-us.txt)... 
    Dictionary successfully loaded: 466544 words were found.
    Valid words: abrin, bairn, brain, brian, brina, rabin
