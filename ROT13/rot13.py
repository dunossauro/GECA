#!/usr/bin/python 3

import string

def cripto(frase):

	alfabeto = string.ascii_uppercase
	saida = ""

	for letra in frase:

		busca = alfabeto.find(letra)+13
		modulo = busca % 26
		saida += str(alfabeto[modulo])

	print(saida)
	input("\n\nPressione Enter para continuar")
