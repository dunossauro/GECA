#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        
        for x in word:
        	print (("%s\t\t%s") % (x, 1))
