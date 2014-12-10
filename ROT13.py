#!/bin/python3.4

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
