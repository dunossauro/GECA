#!/usr/bin/python 3

import string

def cripto(frase, chave):

	alfabeto = string.ascii_uppercase
	saida = ""

	for letra in frase:
	
		if chave is "1":
			busca = alfabeto.find(letra)+3
	
		else:
			busca = alfabeto.find(letra)-3
	
		modulo = busca % 26
		saida += str(alfabeto[modulo])

	print(saida)
	input("\n\nPressione Enter para continuar")
