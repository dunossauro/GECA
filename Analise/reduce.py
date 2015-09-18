#!/usr/bin/env python3
import sys

print (("%-20s|%-7s") % ("Palavra", "Frequência"))
print (("%-20s+-%-7s") % ("-" * 20, "-" * 7))

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split()
    
    count = int(count)

    if current_word == word:
        current_count += int(count)

    else:
        if current_word:
            print (('%-20s:%2s') % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print (('%-20s:%2s') % (current_word, current_count))
