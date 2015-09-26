#!/usr/bin/env python3


import sys
import collections

arquivo = open(sys.argv[1]).read()

arquivo_limpo = [x.upper() for x in arquivo.split() if x.isalpha()]

#FORMULA
N = len(arquivo_limpo)
freqs = collections.Counter(arquivo_limpo)
alfabeto = [chr(x) for x in range(ord("A"),ord("Z")+1)]
soma = 0.0

for letra in alfabeto:
	soma += freqs[letra] * (freqs[letra] -1)

IC = soma/(N*(N-1))

print(IC)
