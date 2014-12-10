#!/bin/python3.4

"""
Sobre:

	Esse programa criptografa usando o ROT13, ou cifra do Kama-Sutra.

	É o desafio de férias número 1 proposto pelo GECA (Grupo de estudos criptográficos de Americana)

Versão:

	0.1 (09/12/2014)

Desevolvedores:
	0.1
		Eduardo F. Mendes (z4r4tustr4)
		Jacomo Giovanetti

Debug:
	0.1
		William Cesar Godoy Lopes (WgL)
"""


frase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(frase)
for x in range(0, len(frase)):
	
	if x < 13:
		for y in range(0, 13):
			
			if frase[x] == alfabeto[y]:
				frase[x] = alfabeto[y+13] 

	else:

		for y in range(13, 26):
			
			if frase[x] == alfabeto[y]:
				frase[x] = alfabeto[y-13]
print(frase)
